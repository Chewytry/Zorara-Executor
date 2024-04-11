import tensorflow as tf
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import io
import os
import cv2


# Load the saved CNN model
def load_cnn_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

# Function to preprocess input image
def preprocess_image(uploaded_file, target_size=(128, 128)):
    # Load the uploaded image
    image = Image.open(uploaded_file)  # Load and resize the image

    # Convert grayscale images to RGB format because the model works with RGB
    if image.mode != 'RGB':
        image = image.convert('RGB')

    img = image.resize(target_size)  # Resize the image
    img_array = img_to_array(img)  # Convert to array
    img_array = img_array / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    print("-----------After reshape----------------------")
    print(img_array.shape)
    return img_array


# Function to perform prediction on an input image
def predict_with_cnn(input_image):
    # Preprocess the input image
    processed_image = preprocess_image(input_image)

    # Load the CNN model
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'cnn_model.h5')
    cnn_model = load_cnn_model(model_path)

    # Make predictions using the loaded model
    predictions = cnn_model.predict([processed_image])
    
    # Return the predictions
    print("------------------------------------")
    print(predictions)
    label = [1 if pred[1] > pred[0] else 0 for pred in predictions]
    return label
