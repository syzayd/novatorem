# Example Flask app for Vercel
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your deployed app!"
