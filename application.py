import os
from flask import Flask, render_template, request, url_for
import numpy as np
import cv2

# Import our library
from mnist_classifier import classify

app = Flask(__name__)

# Render initial page
@app.route("/")
def index():
    return render_template("index.html")

# Render success page, with result from classification
@app.route("/success/<int:number>")
def success(number):
    return render_template("success.html", res=number)

# Receives jQuery POST signal when user submits the digit and triggers the ML script
@app.route('/uploadajax', methods = ['POST'])
def upldfile():
    if request.method == "POST":
       file_val = request.data # Read data on the pad

       fig = cv2.imdecode(np.fromstring(request.data, np.uint8), cv2.IMREAD_UNCHANGED) #Convert from string to cv2 image
       img = cv2.cvtColor(fig, cv2.COLOR_RGB2GRAY) # Convert to grayscale

       classification = classify(img) # Calls the classifier (note argument must be cv2 image or np array)

       return url_for('success', number=int(np.argmax(classification))) # Calls the success page with result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
