from flask import Flask, render_template, request
import os
from core.scanner import scan_folder

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():

    duplicates = []

    if request.method == "POST":

        files = request.files.getlist("files")

        for file in files:
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

        duplicates = scan_folder(app.config["UPLOAD_FOLDER"])

    return render_template("index.html", duplicates=duplicates)

if __name__ == "__main__":
    app.run(debug=True)