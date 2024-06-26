#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Load auth based on AUTH_TYPE environment variabl
auth = None
AUTH_TYPE = getenv("AUTH_TYPE", None)

if AUTH_TYPE:
    if AUTH_TYPE == "auth":
        from api.v1.auth.auth import Auth
        auth = Auth()
    if AUTH_TYPE == "basic_auth":
        from api.v1.auth.basic_auth import BasicAuth
        auth = BasicAuth()
    if AUTH_TYPE == "session_auth":
        from api.v1.auth.session_auth import SessionAuth
        auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler """
    return jsonify({"error": "Forbidden"}), 403


# Define the before_request handler
@app.before_request
def before_request():
    """ Performs authentication and authorization checks before each request.
    """
    if auth is None:
        return

    # Paths that don't require authentication
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/']

    # Check if the path requires authentication
    if not auth.require_auth(request.path, excluded_paths):
        return

    # Check for valid authorization header or session cookie
    if not auth.authorization_header(request) \
            and not auth.session_cookie(request):
        abort(401)  # Unauthorized

    # Check if current user is authenticated
    if auth.current_user(request) is None:
        abort(403)  # Forbidden

    request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
