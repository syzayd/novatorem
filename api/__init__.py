# __init__.py

import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Spotify scopes required by your app
SPOTIFY_SCOPES = [
    "user-read-currently-playing",
    "user-read-recently-played"
]

# Placeholder image base64 string (truncated here for clarity)
PLACEHOLDER_IMAGE = (
    "iVBORw0KGgoAAAANSUhEUgAAA4QAAAOEBAMAAAALYOIIAAAAFVBMVEXm5ub///8AAAAxMTG+vr6RkZFfX1/R+IhpAAAfE0lEQVR42uzdS3fayBaG..."
)

# Create Flask app instance
app = Flask(__name__)

# Import your main routes or logic here to register routes with the app
# from . import routes  # if you split routes into a separate file

# You can place your spotify.py logic here or import functions/classes as needed
# For example:
# from .spotify import some_function

# This makes the app available when you do: from yourpackage import app
