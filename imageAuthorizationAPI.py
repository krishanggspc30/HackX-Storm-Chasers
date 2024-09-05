from flask import Flask, request, jsonify
from google.cloud import vision
import os

app = Flask(__name__)

# Set up your Google Cloud Vision client
client = vision.ImageAnnotatorClient()

# Function to detect labels
def detect_labels(image_path):
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    label_descriptions = [label.description.lower() for label in labels]  # Convert labels to lowercase
    return label_descriptions

# Function to check for specific labels
def contains_keywords(labels):
    # Define the keywords to check for
    keywords = {'bin bag', 'waste container', 'plastic bag', 'pollution', 'waste', 'trash'}
    
    # Check if any of the keywords are in the labels
    return any(keyword in labels for keyword in keywords)

# API endpoint for object detection
@app.route('/detect-labels', methods=['POST'])
def detect_labels_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    image_path = os.path.join('uploads', image.filename)
    image.save(image_path)

    try:
        labels = detect_labels(image_path)
        has_keywords = contains_keywords(labels)
        return jsonify({'labels': labels, 'contains_keywords': has_keywords})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Cleanup the uploaded image after processing
        os.remove(image_path)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
