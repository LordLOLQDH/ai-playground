import cv2
import numpy as np

def load_image(image_path):
    return cv2.imread(image_path)

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply adaptive thresholding
    _, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)
    
    return binary

def texture_image(image, texture_map):
    # Resize the texture map to match the image size
    texture_map = cv2.resize(texture_map, (image.shape[1], image.shape[0]))
    
    # Apply the texture map to the image
    textured_image = cv2.addWeighted(image, 0.5, texture_map, 0.5, 0)
    
    return textured_image

# Example usage
image_path = 'path_to_your_image.jpg'
texture_map_path = 'path_to_your_texture_map.png'

image = load_image(image_path)
texture_map = load_image(texture_map_path)

preprocessed_image = preprocess_image(image)
textured_image = texture_image(preprocessed_image, texture_map)

cv2.imshow('Textured Image', textured_image)
cv2.waitKey(0)
cv2.destroyAllWindows()