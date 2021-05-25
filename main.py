import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import Form, SubmitField

from modules.PCA.PlotPCA import Plot

app = Flask(__name__) 

app.config["DEBUG"] = True
app.config["SECRET_KEY"]="PUMAV2"
#Upload folder
UPLOAD_FOLDER = 'static/files/'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def parseCSV(filepath):
    csvData = pd.read_csv(filepath)
    print(csvData.head())
    return "file loaded"

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home2")
def home_2():
    return render_template("home2.html")


@app.route("/home2", methods = ["POST"])
def file():
    uploaded_file = request.files["file"]
    if uploaded_file.filename != "":
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
        uploaded_file.save(file_path)
        print("file is loaded")
    return redirect(url_for("home_2"))
    # return "file was loaded"


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


"""Chemical Space"""
class ChemSpaceForm(Form):
    pca = SubmitField('pca')
    tsne  = SubmitField('tsne')





@app.route("/select_chemspace", methods = ["GET","POST"])
def select_chemspace():
    print("starting form")
    form = ChemSpaceForm(request.form)
    if request.method == 'POST' :
    # if form.validate_on_submit():
        if form.pca.data:
            return redirect(url_for('plot_1'))
        if form.tsne.data:
            return "TSNE will be displayed"
    return render_template("select_chemspace.html", form=form)

@app.route("/plot_1")
def plot_1():
    result = pd.read_csv("/home/babs/Desktop/test_puma/PCA_result_test_puma_2.csv")
    print(result.head(4))
    script, div = Plot(result).plot_pca("physicochemical descriptors", "50","50")
    return render_template("plot.html", script=script, div=div)
    

if (__name__ == "__main__"):
    app.run(port=5000, debug=True) 
