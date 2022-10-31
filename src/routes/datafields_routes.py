from flask import Blueprint
import controllers.datafields_controllers as Controller
from flask_cors import cross_origin

datafieldsRoutes = Blueprint("datafields", __name__, url_prefix="/datafields")


@datafieldsRoutes.route("/", methods=["GET"])
@cross_origin()
def CargarDataFields():
    return Controller.CargarDataFields()
