from flask import jsonify
import models.datafields_models as Model


def CargarDataFields():
    return jsonify(Model.CargarDataFields())
