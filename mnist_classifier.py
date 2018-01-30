import sys
from keras.models import Model, load_model
import numpy as np
from cv2 import imread

# Import image converter
from fig_to_mnist import mnist_treat

def classify(fig):

    # Standard MNIST format is 28x28 pixels and grayscale.
    height, width, depth = 28, 28, 1

    # Proccess image (c.f. fig_to_misc.py) and convert to numpy array
    X = mnist_treat(fig)
    X_array = np.array(X)

    # Flatten image
    X_flat = X_array.reshape(1, height * width)

    # Normalize to 1 = white.
    X_flat = X_flat.astype('float32')
    X_flat /= 255

    # Load trained model. In this case, a two layer dense NN with 512 hidden neurons.
    model = load_model('MNIST_twolayers.h5')

    # Run prediction
    prediction = model.predict(X_flat, verbose=0)

    return(prediction)
