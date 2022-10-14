from flask import Blueprint
import controllers.recibos_controllers as Controller

recibosRoutes = Blueprint("recibos", __name__, url_prefix="/recibos")


@recibosRoutes.route("/<nivel>/<codigogrupo>/<periodo>/<mes>", methods=["GET"])
def GenerarTickets(nivel, codigogrupo, periodo, mes):
    return Controller.GenerarTicket(nivel, codigogrupo, periodo, mes)
