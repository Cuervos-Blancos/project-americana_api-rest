import json
from os.path import exists
from flask import jsonify
import models.recibos_models as Model


def GenerarTicket(nivel, codigogrupo, periodo, mes):
    # obtiene los tickets de la base de datos
    res_db = Model.GenerarTickets(nivel, codigogrupo, periodo, mes)
    resToSend = []

    # agregamos el campo de enviado
    for alumno in res_db:
        alumno["enviado"] = "no"

    # verificamos si el archivo existe
    if exists(f"log_files/{nivel}_{codigogrupo}_{periodo}_{mes}.json"):

        # abre el archivo
        with open(f"log_files/{nivel}_{codigogrupo}_{periodo}_{mes}.json", "r") as openFile:
            json_object = json.load(openFile)

        # verifica si existe el alumno en el log
        for alumno in res_db:
            for index, item in enumerate(json_object):
                if (alumno["numeroalumno"] == item["numeroalumno"]):
                    # print("esta en log")
                    # comprueba que el campo enviado sea el mismo
                    a = json_object[index]
                    resToSend.append(a)
                    break

            else:
                # print("no esta en log")
                resToSend.append(alumno)

        # vuelve a serialize el json

        # Serializing json
        json_object = json.dumps(resToSend, indent=4)

        # Writing to sample.json
        with open(f"log_files/{nivel}_{codigogrupo}_{periodo}_{mes}.json", "w") as outfile:
            outfile.write(json_object)

        return (resToSend)

    else:
        # Serializing json
        json_object = json.dumps(res_db, indent=4)

        # Writing to sample.json
        with open(f"log_files/{nivel}_{codigogrupo}_{periodo}_{mes}.json", "w") as outfile:
            outfile.write(json_object)

        return jsonify(res_db)
