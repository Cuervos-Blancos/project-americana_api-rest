from flask import Blueprint
import controllers.mobile_controllers as Controller

mobileRoutes = Blueprint("mobile", __name__, url_prefix="/mobile")


@mobileRoutes.route("/<numeroalumno>", methods=["GET"])
def ObtenerCamposAlumno(numeroalumno):
    return Controller.ObtenerCamposAlumno(numeroalumno)
