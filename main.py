import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 

app.config["DEBUG"] = True

#Upload folder
UPLOAD_FOLDER = 'static/files'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def parseCSV(filepath):
    csvData = pd.read_csv(filepath)
    print(csvData.head())
    return "file loaded"

@app.route("/")
def index():
    return render_template("home.html")

#get the uoloaded file
@app.route("/", methods = ["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    if uploaded_file.filename != "":
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
        uploaded_file.save(file_path)
        #read_csv
        parseCSV(file_path)
    return redirect(url_for("index"))

@app.route("/select_chemspace")
def select_chemspace():
    return render_template("select_chemspace.html")

if (__name__ == "__main__"):
    app.run(port=5000) 
