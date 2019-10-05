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
        return respond(user, 200)
    else:
        return error("Invalid credentials", 403)
