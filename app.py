from flask import Flask
from flask import render_template
from flask import request

from PIL import Image

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            flash("")

    file = request.files["uploadFile"]
    

if __name__ == "__main__":
    app.run(debug=True)
