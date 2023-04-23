from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import controllers.logIn_controllers as Controller

logInRoutes = Blueprint("login", __name__, url_prefix="/login")


@logInRoutes.route("/", methods=["POST"])
@cross_origin()
def LogIn():
    parametros = request.json
    resp = Controller.LogIn(parametros["username_email"], parametros["password"])
    if resp == "ok":
        return jsonify(resp), 200
    if resp == "error":
        return jsonify(resp), 500
