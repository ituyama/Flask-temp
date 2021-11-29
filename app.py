from flask import Flask,render_template,request,redirect,url_for,flash 
import numpy as np

from PIL import Image
import os

from flask import send_from_directory

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(__name__)

    ## all rights reserved Yamano 2021
@app.route('/', methods=['GET', 'POST'])
def mains():

    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def yamano():
    fs = request.files['file']

    
    filename = fs.filename

    img_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    fs.save(img_url)


    return render_template("upload.html",url=img_url)
    
@app.route('/uploads/<filename>')
# ファイルを表示する
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
## おまじない
if __name__ == "__main__":
    app.run()
    ## all rights reserved Yamano 2021