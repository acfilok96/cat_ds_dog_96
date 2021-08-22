from flask import Flask, render_template, request
import os
from PIL import Image 
import PIL 
import numpy as np
from tensorflow.keras.models import model_from_json

json_file = open('cat_vs_dog_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
        
app = Flask(__name__)
PATH = "uploads/"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about", methods=["POST"])
def about():
    secure_path = ""
    del secure_path
    if request.method == "POST":
        image_file = request.files["image_file"]
        path = os.path.join(PATH, image_file.filename)
        image_file.save(path)
        secure_path = path
        img_path = Image.open(path)
        img_path = np.asarray(img_path)
        img_path = img_path.reshape((1, 500, 500, 3))
        pred = loaded_model.predict(img_path)
        pred = np.argmax(pred)
        name_spices = "CAT"
        if pred == 1:
            name_spices = "DOG"
        return render_template("index.html", result = str(name_spices))

if __name__ == "__main__":
    app.run(debug=True)
