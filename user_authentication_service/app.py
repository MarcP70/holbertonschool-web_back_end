#!/usr/bin/env python3
"""Flask app module
"""
from flask import Flask, jsonify, request
from auth import Auth


# Create the Flask application
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """Welcome methode to return a welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """Register methode to register a user if not already exist
    """
    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    try:
        user = AUTH.register_user(email, password)

        return jsonify({
            "email": user.email,
            "message": "user created"
        }), 200

    except ValueError:
        return jsonify({
            "message": "email already registered"
        }), 400


# Run the Flask application if this script is run directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
