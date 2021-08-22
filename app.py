from flask import Flask, render_template, request, url_for

        
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about", methods=["POST"])
def about():
    if request.method == "POST":
        image_file = request.files["image_file"]
        path = url_for('static',filename= image_file.filename )
        
        return render_template("index.html", result = str(path))

if __name__ == "__main__":
    app.run(debug=True)
