from flask import Blueprint
from flask_cors import cross_origin
import controllers.mobile_controllers as Controller

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

mobileRoutes = Blueprint("mobile", __name__, url_prefix="/mobile")


@mobileRoutes.route("/<numeroalumno>", methods=["GET"])
@cross_origin()
def ObtenerCamposAlumno(numeroalumno):
    meses = {
        1: "5",
        2: "6",
        3: "7",
        4: "8",
        5: "9",
        6: "10",
        7: "11",
        8: "12",
        9: "1",
        10: "2",
        11: "3",
        12: "4",
    }

    m = datetime.now()
    meses_str = ""
    for i in range(3):
        meses_str = meses_str + meses[(m - relativedelta(months=i)).month] + ", "
    print(meses_str[: len(meses_str) - 2])

    return Controller.ObtenerCamposAlumno(numeroalumno)
