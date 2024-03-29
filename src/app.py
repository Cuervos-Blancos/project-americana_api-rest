# IMPORTACIONES
from http.client import HTTPException
from flask import Flask, jsonify
from flask_cors import CORS
import os
import config
from routes.datafields_routes import datafieldsRoutes
from routes.recibos_routes import recibosRoutes
from routes.mobile_routes import mobileRoutes
from routes.mail_routes import mailRoutes
from routes.logIn_routes import logInRoutes


# CONFIGURACIONES E INICIO
application = Flask(__name__)
# CORS(application)
cors = CORS(application, resources={r"/*": {"origins": "*"}})

if os.getenv("ENV") == "DEVELOPMENT":
	application.config.from_object(config.DevelopmentConfig)
else:
	application.config.from_object(config.ProductionConfig)


# ERROR 404
@application.errorhandler(404)
def route_not_found(err):
	return jsonify({"message": "Ruta no encontrada"}), 404


@application.errorhandler(500)
def internal_server_err(err):
	return jsonify({"message": "Ha ocurrido un error en el servidor"}), 500


# OTROS ERRORES


# INDEX ROUTE
@application.route("/", methods=["GET"])
def Home():
	return (
		jsonify(
			{
				"name": "rest_api_python3-firebird",
				"authors": ["Carlos C.", "Abarca Lopez"],
				"description": "Modulo de RestApi del proyecto de automatización de envio de correos electronicos para la Americana",
				"version": "0.1",
			}
		),
		200,
	)


# * ROUTES
application.register_blueprint(recibosRoutes)
application.register_blueprint(datafieldsRoutes)
application.register_blueprint(mobileRoutes)
application.register_blueprint(mailRoutes)
application.register_blueprint(logInRoutes)
