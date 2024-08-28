# PassportScrapper

## Overview

**PassportScrapper** is a Flask-based web application designed to extract relevant information from passport images. The application uses image processing techniques with OpenCV and Optical Character Recognition (OCR) with Tesseract to identify and extract key details such as passport number, name, nationality, date of birth, and more.

## Features

- **Upload Passport Image**: Users can upload a passport image to extract the embedded information.
- **Image Processing**: The uploaded image is processed using OpenCV to enhance its quality before OCR is applied.
- **Data Extraction**: Pytesseract is used to perform OCR on the processed image, extracting text data with a focus on passport-related details.
- **User Interface**: A clean and simple web interface using Bootstrap for easy interaction.

## Technologies Used

- **Flask**: A micro web framework used for the backend of the application.
- **OpenCV**: A library for image processing to enhance the quality of the uploaded passport image.
- **Pytesseract**: A Python wrapper for Google’s Tesseract-OCR Engine, used for extracting text from images.
- **Bootstrap**: A front-end framework used to style the web pages.
- **PIL (Pillow)**: A Python Imaging Library that adds image processing capabilities.

## Setup and Installation

### Prerequisites

- Python 3.12
- Pip (Python package installer)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/4TechSadiq/PassScrapper-WEB.git
    cd PassportScrapper-WEB
    ```

2. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Tesseract-OCR:**

    - **Windows:** [Download the Tesseract installer](https://github.com/UB-Mannheim/tesseract/wiki).
    - **Linux:** Install via package manager, e.g., `sudo apt-get install tesseract-ocr`.
    - **MacOS:** Install via Homebrew, `brew install tesseract`.

5. **Configure Pytesseract Path:**

    If necessary, specify the path to Tesseract in your code, e.g., `pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`.

### Running the Application

1. **Start the Flask Application:**

    ```bash
    python app.py
    ```

2. **Access the Application:**

    Open a web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Upload a Passport Image:**
    - Click on the file input field to select and upload your passport image.
    - Click the "Extract Data" button to begin the extraction process.

2. **View Extracted Data:**
    - The extracted information will be displayed on the same page.

## Example
**Output:**

```json
{
    "PASSNO": "A1234567",
    "SURNAME": "DOE",
    "GIVENNAME": "JOHN MICHAEL",
    "NATIONALITY": "INDIAN",
    "C_CODE": "IND",
    "DOB": "01-01-1990",
    "DOI": "15-05-2015",
    "DOE": "14-05-2025",
    "GENDER": "M",
    "POB": "MUMBAI, MAHARASHTRA",
    "POE": "MUMBAI"
}
