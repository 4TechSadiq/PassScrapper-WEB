from flask import render_template, Flask, request
from scrapper import extract_passport_info  # Ensure this module is correctly defined
from PIL import Image

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("yesssss")
        try:
            if 'picture' in request.files:
                print("yes")
                image = request.files['picture']
                with Image.open(image) as img:
                    data = extract_passport_info(img)
                    print(data)
                if data:
                    return render_template("index.html", data=data)
                else:
                    return render_template("index.html", error="Error Occurred While Extraction")
            else:
                return render_template("index.html", error="No file uploaded.")
        except Exception as e:
            return render_template("index.html", error=f"An error occurred: {e}")
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
