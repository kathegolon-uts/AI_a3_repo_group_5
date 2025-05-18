import pandas as pd
import random

# Mapping from Hugging Face detected emotions → Moodify moods
emotion_to_mood = {
    'angry': 'sad',
    'disgust': 'sad',
    'fear': 'sad',
    'sad': 'sad',
    'happy': 'happy',
    'surprise': 'energetic',
    'neutral': 'calm'
}

def load_moodify_dataset(filepath: str) -> pd.DataFrame:
    """
    Load the Moodify dataset.
    Expects a CSV with at least:
      - 'labels' column: 0=sad, 1=happy, 2=energetic, 3=calm
      - 'uri' column: Spotify URI (spotify:track:...)
    """
    return pd.read_csv(filepath)

def map_emotion_to_mood(emotion: str) -> str:
    """
    Map a detected emotion to one of the Moodify categories.
    Defaults to 'calm' if the emotion isn't recognised.
    """
    return emotion_to_mood.get(emotion.lower(), 'calm')

def recommend_song(moodify_df: pd.DataFrame, mood: str) -> str:
    """
    Given the loaded dataset and a mood label, randomly select a matching track URI.
    Returns the full Spotify URI (e.g. 'spotify:track:...') or None if no match.
    """
    # Numeric labels in the CSV
    mood_label_map = {
        'sad': 0,
        'happy': 1,
        'energetic': 2,
        'calm': 3
    }
    label = mood_label_map.get(mood)
    if label is None:
        return None

    matching = moodify_df[moodify_df['labels'] == label]
    if matching.empty:
        return None

    selected = matching.sample(1).iloc[0]
    return selected['uri']
