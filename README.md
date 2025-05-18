# Melofy: The AI Mood-Based Music Recommendation System 🎵😊

## Overview

This project is part of the final assignment for the subject Artificial Intelligence Principles and Applications at UTS.
We built an AI-based system that recommends music based on users' detected facial emotions using Streamlit and facial recognition.

## Project Flow
1. User opens the app and takes a selfie.
2. The system analyses the image to detect the user's emotion.
3. The detected emotion is mapped to a music mood.
4. The app recommends songs accordingly.

## Local Setup Instructions

To ensure everyone in the group uses the same Python version and dependencies, we use:
* pyenv to manage the Python version
* poetry to manage the environment and packages

### Prerequisites
* [Pyenv installed](https://github.com/pyenv/pyenv)
* [Poetry installed](https://python-poetry.org/docs/)

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/kathegolon-uts/AI_a3_repo_group_5.git
cd AI_a3_repo_group_5

# Set Python version
pyenv install 3.11.4    # Only if not already installed
pyenv local 3.11.4      # Enforces the project Python version

# Create and activate the virtual environment
poetry install          # Installs all dependencies
poetry shell            # Activates the environment
```

## Running the App 🚀

After activating the poetry shell:
```bash
streamlit run app.py
```

## Project Structure
```bash
AI_a3_repo_group_5/
│
├── .venv/                     # Local virtual environment (excluded from repo)
├── data/
│   ├── 278k_labelled_uri.csv  # Moodify dataset (Spotify URIs and mood labels)
│   └── FER-2013/              # FER-2013 facial emotion dataset (local use only)
│
├── notebooks/
│   ├── moodify_eda.ipynb      # EDA on Moodify dataset
│   └── facial-expression-recognition.ipynb  # Model testing on FER-2013
│
├── reports/
│   └── AI_a3_report_24611687.pdf  # Final report (PDF version)
│
├── src/
│   ├── __init__.py
│   ├── emotion_detection.py   # Emotion detection using Hugging Face ViT
│   └── music_recommender.py   # Mood mapping and song recommendation logic
│
├── app.py                     # Streamlit frontend application
├── requirements.txt           # Dependency list (used by Streamlit Cloud)
├── poetry.lock                # Poetry lock file for package versions
├── pyproject.toml             # Poetry configuration (project + dependencies)
├── README.md                  # Project overview and setup instructions
├── .gitignore                 # Ignore virtual environments and cache
└── .python-version            # Python version config for Pyenv

```

## Contributors
* Katherin Gomez Londono
* Dipesh Shrestha
* Jaime Garcia y Garcia
* Miguel Ramal
* Spenser Gautama

# 🚀 AI that feels the music!