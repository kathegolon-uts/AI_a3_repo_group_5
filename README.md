# AI Mood-Based Music Recommendation System 🎵😊

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
├── notebooks/                      # EDA and preprocessing
├── reports/                        # Final Report and Slides
├── src/                            # Source code folder
│   ├── __init__.py                 # (empty) marks src as a package
│   ├── emotion_detection.py        # Emotion detection functions
│   ├── music_recommender.py        # Music mood mapping + song recommendation
│
├── .gitignore                      # Keep repo clean (ignoring temp files, cache, etc.)
├── .python-version                 # Python version control
├── app.py                          # Streamlit main app
├── pyproject.toml                  # Poetry dependency management
├── README.md                       # Project documentation

```

## Contributors
* Katherin Gomez Londono
* Dipesh Shrestha
* Jaime Garcia y Garcia
* Miguel Ramal
* Spenser Gautama

# 🚀 AI that feels the music!