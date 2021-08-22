from flask import Flask, render_template, request
import cv2
from PIL import Image
import numpy as np
from keras.models import model_from_json

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
        img = cv2.imread(img_path)
        resized = cv2.resize(img, (500, 500))
        resized = resized.reshape((1, 500, 500, 3))
        pred = loaded_model.predict(resized)
        pred = np.argmax(pred)
        name_spices = "CAT"
        if pred == 1:
            name_spices = "DOG"
        return render_template("index.html", result = str(name_spices))

if __name__ == "__main__":
    app.run(debug=True)
