from flask import Flask, render_template, request
import cv2, os
import numpy as np

app = Flask(__name__)
PATH = "uploads"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about", methods=["POST"])
def about():
    if request.method == "POST":
        image_file = request.files["image_file"]
        path = PATH+"/"+str(image_file.filename)
        image_file.save(path)
        secure_path = path
        img = cv2.imread(path)
        resized = cv2.resize(img, (500, 500))
        resized = resized.reshape((1, 500, 500, 3))
        shaped = resized.shape
        os.remove(secure_path)
        return render_template("index.html", result = str(shaped))

if __name__ == "__main__":
    app.run(debug=True)
