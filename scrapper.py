import cv2
import pytesseract
import numpy as np
import re
import json
from PIL import Image

def extract_passport_info(image):
    try:
        # Convert the PIL Image to a NumPy array
        image_np = np.array(image)

        if image_np is None:
            raise ValueError("Image not found or unable to load.")
        
        gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        sharpened = cv2.filter2D(image_np, -1, kernel)
        denoised_image = cv2.fastNlMeansDenoisingColored(sharpened, None, 10, 10, 7, 21)
        gray_denoised = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2GRAY)
        
        detection = pytesseract.image_to_data(denoised_image, output_type=pytesseract.Output.DICT)
        
        detected_texts = []

        for i in range(len(detection['text'])):
            try:
                if detection['text'][i] and int(detection['conf'][i]) > 60:
                    detected_texts.append(detection['text'][i])
            except Exception as e:
                print(f"Error processing detection index {i}: {e}")
        
        # Define regex patterns
        s_pattern = r'\b[M|F]\b'
        pno_pattern = r'\b[A-Z]\d{7}\b'
        d_pattern = r'\b((0[1-9]|[12]\d|30)[-/](0[1-9]|1[0-2])[-/]\d{4}|\d{4}[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|30))\b'
        n_pattern = r'\bINDIAN\b'
        c_pattern = r'\bIND\b'
        words_pattern = r'\b(?!(?:INDIA|INDIAN|GOVERNMENT OF INDIA|GOVERNMENT|REPUBLIC|OF)\b)\b[A-Z]{4,}\b'
        
        # Initialize variables
        PASSNO = None
        SURNAME = None
        FULLNAME = None
        NATIONALITY = None
        C_CODE = None
        DOB = None
        DOI = None
        DOE = None
        GENDER = None
        POB = None
        POE = None
        words = []
        dates = []
        
        # Extract the information using regex
        for text in detected_texts:
            try:
                if re.search(s_pattern, text):
                    GENDER = re.search(s_pattern, text).group()

                if re.search(pno_pattern, text):
                    PASSNO = re.search(pno_pattern, text).group()

                if re.search(n_pattern, text):
                    NATIONALITY = re.search(n_pattern, text).group()

                if re.search(c_pattern, text):
                    C_CODE = re.search(c_pattern, text).group()

                if re.findall(words_pattern, text):
                    words.extend(re.findall(words_pattern, text))

                if re.findall(d_pattern, text):
                    dates.extend(re.findall(d_pattern, text))
            except Exception as e:
                print(f"Error processing text '{text}': {e}")

        # Assign the extracted values
        if len(dates) > 0:
            DOB = dates[0]
        if len(dates) > 1:
            DOI = dates[1]
        if len(dates) > 2:
            DOE = dates[2]


        DOB = DOB[0] if DOB and isinstance(DOB, list) else DOB
        DOI = DOI[0] if DOI and isinstance(DOI, list) else DOI
        DOE = DOE[0] if DOE and isinstance(DOE, list) else DOE

        if words:
            SURNAME = words[0]
        if len(words) >= 3:
            POE = words[-1]
            POB = words[-3] + ", " + words[-2]
        if len(words) >= 5:
            FULLNAME = " ".join(words[1:3])

        # Create the JSON response
        passport_info = {
            "PASSNO": PASSNO,
            "SURNAME": SURNAME,
            "GIVENNAME": FULLNAME,
            "NATIONALITY": NATIONALITY,
            "C_CODE": C_CODE,
            "DOB": DOB[0] if DOB else None,
            "DOI": DOI[0] if DOI else None,
            "DOE": DOE[0] if DOE else None,
            "GENDER": GENDER,
            "POB": POB,
            "POE": POE
        }
        
        return json.dumps(passport_info, indent=4)

    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)
