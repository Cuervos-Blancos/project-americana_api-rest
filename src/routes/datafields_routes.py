from flask import Blueprint
import controllers.datafields_controllers as Controller

datafieldsRoutes = Blueprint("datafields", __name__, url_prefix="/datafields")


@datafieldsRoutes.route("/", methods=["GET"])
def CargarDataFields():
    return Controller.CargarDataFields()
