import json
from flask import (
    current_app as app,
    Blueprint,
    request
)
from requests import respond, error
import api.accounts.services as services

accounts = Blueprint(
    'accounts',
    __name__
)

@accounts.route("/authenticate", methods=["POST"])
def authenticate():
    email = request.form["email"]
    password = request.form["password"]

    user = services.authenticate(
        email,
        password
    )

    if user:
        session_id = services.generate_session_token(user[0]["id"])
        return respond({ **user[0], "session_id": session_id }, 200)
    else:
        return error("Invalid credentials", 403)
