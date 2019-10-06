from flask import jsonify


def respond(payload, status, mimetype="application/json"):
    return jsonify(payload), status


def error(msg, status):
    return jsonify({"Error": msg}), status
