import json
from flask import current_app as app, Blueprint, request
from requests import respond, error
import api.issues.services as services

issues = Blueprint("issues", __name__)


@issues.route("/", methods=["GET", "PUT", "POST", "DELETE"])
def issue():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        issue = services.create_issue(request.form)
        if not issue:
            return error("There was an error creating a new issue.", 500)
        else:
            return respond({"Message": "New issue has been created."}, 200)
