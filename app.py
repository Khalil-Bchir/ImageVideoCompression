from flask import Flask
from flask_cors import CORS
from App.routes import app  # assuming you've defined 'app' in routes.py

# Enable CORS for all routes
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
