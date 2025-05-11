from transformers import pipeline
import tempfile

# Load the model ONCE at module level
emotion_pipeline = pipeline(model='shrestha1/vit-Facial-Expression-Recognition')

def detect_emotion(image_file):
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(image_file.getvalue())
        tmp_path = tmp_file.name

    # Run the model on the temp file
    predictions = emotion_pipeline(tmp_path)

    # Find the label with the highest score
    best_pred = max(predictions, key=lambda x: x['score'])
    detected_emotion = best_pred['label']

    return detected_emotion
