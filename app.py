from flask import Flask, render_template, request

        
app = Flask(__name__)
PATH = "/uploads"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about", methods=["POST"])
def about():
    if request.method == "POST":
        image_file = request.files["image_file"]
        path = PATH+"/"+str(image_file.filename)
        image_file.save(path)
        
        return render_template("index.html", result = str(path))

if __name__ == "__main__":
    app.run(debug=True)
