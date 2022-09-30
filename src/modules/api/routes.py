from flask import Blueprint, jsonify, make_response
from modules.api.controllers import SelectAlumnosPrepa, SelectCxC


apiRoutes = Blueprint("api", __name__, url_prefix="/api")


@apiRoutes.route("/alumnosprepa", methods=["GET"])
def Alumnos():
    resultado = SelectAlumnosPrepa()
    return make_response(jsonify(resultado), 200)


@apiRoutes.route("/cxc", methods=["GET"])
def CxC():
    try:
        listaAlumnos = SelectAlumnosPrepa()
        resultado = []

        for alumno in listaAlumnos:
            datos = SelectCxC(alumno)
            if datos:
                merged = alumno | datos
                resultado.append(merged)
        
        return make_response(jsonify(resultado), 200)
    except Exception as e:
        print("EXCEPTION from  modules>api>routes.py>CxC(): ", e)
        return make_response({"message": "ha ocurrido un error inesperado"}, 500)


""" @apiRoutes.route("/niveles", methods=["GET"])
def Niveles():
    alumnos = SelectAlumnosPrepa()
    res = SelectNivel(alumnos)
    return make_response(jsonify(res)) """
