#!/usr/bin/env python3
"""Flask app
"""
from flask import Flask, jsonify


# Create the Flask application
app = Flask(__name__)


@app.route("/")
def welcome():
    """ Welcome methode
    """
    return jsonify({"message": "Bienvenue"})


# Run the Flask application if this script is run directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
