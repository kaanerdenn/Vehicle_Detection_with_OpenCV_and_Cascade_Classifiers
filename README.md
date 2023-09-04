# Vehicle_Detection_with_OpenCV_and_Cascade_Classifiers

This project demonstrates vehicle detection using OpenCV in Python. It processes images to detect cars and buses using Haar Cascade Classifiers. The project involves image resizing, grayscale conversion, Gaussian blurring, dilation, and morphological operations to identify and annotate vehicles in the images.

## Image Processing

### Image Download and Resizing

The project begins by downloading an image from a URL and resizing it to a specified dimension (450x250) using the Pillow (PIL) library.

### Grayscale Conversion

The resized image is converted to grayscale to simplify subsequent processing steps.

### Image Preprocessing

1. **Gaussian Blurring**: A Gaussian blur is applied to the grayscale image to reduce noise and improve detection accuracy.

2. **Dilation**: A morphological dilation operation is performed on the blurred image to enhance the features of interest.

3. **Morphological Closing**: Morphological closing is applied to further refine the image for object detection.

## Vehicle Detection

### Car Detection

Car detection is performed using a Haar Cascade Classifier trained for car detection. The `detectMultiScale` method is used to identify cars in the processed image.

### Bus Detection

Bus detection is also performed using a Haar Cascade Classifier trained for bus detection. The `detectMultiScale` method identifies buses in the image.

## Result Display

The detected cars and buses are annotated with rectangles drawn around them in red (cars) and blue (buses). The total number of cars and buses found in the image is displayed.

The annotated images are displayed using the Pillow (PIL) library.

## Usage

1. To run the script, provide the URL of the image you want to process in the `image_url` variable.

2. Ensure that the Haar Cascade Classifier XML files for car and bus detection are available and correctly specified in the `car_cascade_src` and `bus_cascade_src` variables.

3. Run the script to perform vehicle detection and visualize the results.

4. Press any key to close the displayed image windows.

## Example Usage

An example image is provided, and the script is applied to detect buses in the image.

For more details and specific code implementations, please refer to the project's Python script.
