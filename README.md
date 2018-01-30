# MNIST-pad
*Web app for real time neural network digit classification*

When I was playing with neural networks for the first time using Keras I found frustrating 
that I could not easily input my own handwritten digits to test the classifier. So to practice I have 
combined the Python classifier with a JS web Canvas using Flask. 

The model is the simplest deep neural network, a dense NN with two hidden layers (512 neurons) with 
[ReLu activation](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) and a [softmax](https://en.wikipedia.org/wiki/Softmax_function) output. It was trained with 60000 images from the MNIST database and 
minimizing the crossentropy using the Adam optimizer. The accuracy is approx. 97%.

The Canvas was adapted from @szimek Signature pad (https://github.com/szimek/signature_pad).

## Requirements

For this to run properly you will need the following Python packages:
  * Flask
  * OpenCV (for Python)</li>
  * [TensorFlow](https://www.tensorflow.org/install/)
  * [Keras](https://keras.io/)

As well as the usual numpy and scipy. To install Flask and OpenCV, type in the command line:
```
pip install flask
pip install opencv-python
```
For Keras and TensorFlow, please refer to the links for installing properly.

## Running
Once you have everything set, just go to the repository and call
```
python application.py
```
You should see something like
```
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 338-114-640
```
Now open your browser and access the address http://0.0.0.0:5000/ .

Now draw a digit between 0 and 9 in the canvas and if the neural network can guess it correctly!

## To do
So if you have arrived here you probably realised this code is a bit dirty. In particular what concerns the web part.
This is for two reasons: first I am a physicist, and second because I know very little js. It would be great to

* Do the image processing directly in js, so no need for `fig_to_mist.py`.
* Getting rid of the success page and giving the result directly in the canvas page (but still in a funny way). Or improving the success page.
* Taking out the jQuery from the index.html.

From the ML side, it would be cool to:
* Have more than one model, so that user can choose another one.
* Having the user to say if the classification is right or not, and save the image with correct classification. So we can have a counter of success.

