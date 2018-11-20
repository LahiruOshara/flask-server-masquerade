import os
import cv2
import numpy as np
from flask import Flask,request
import base64
app = Flask(__name__)

port=5000

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def send_file():
    img = cv2.imread('./uploaded_file.jpg')
    _, img_encoded = cv2.imencode('.jpg', img)
    """f=open('uploaded_file.jpg','rb')
    img=f.read()
    f.close()"""
    data=img_encoded.tostring()
    return data

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print ('post request')
        img_file=open('uploaded_file.jpg','wb')
        string_image = request.form['the_file']
        #print(string_image)
        f=base64.decodestring(string_image.encode())
        img_file.write(f)
        img_file.close()
        return ("done")#send_file()