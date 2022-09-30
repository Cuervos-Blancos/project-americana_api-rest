import os
from flask import Flask, make_response
from dotenv import load_dotenv
from modules.api.routes import apiRoutes

# Instancia
app = Flask(__name__)


# RUTAS
@app.route("/", methods=["GET"])
def Home():
    return make_response(
        {
            "name": "rest_api_python3-firebird",
            "authors": ["🍃 Carlos C.", "Abarca Lopez"],
            "description": "Rest Api con python3, flask y firebird driver",
            "version": "0.1",
        },
        200,
    )


app.register_blueprint(apiRoutes)

# Error handler
def NotFound(error):
    return {"message": "path not found"}


app.register_error_handler(404, NotFound)


# Config
load_dotenv()
if os.getenv("ENV") == "development":
    app.config.from_object("app.config.DevelopmentConfig")
    print("THIS IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION")

if os.getenv("ENV") == "production":
    app.config.from_object("app.config.ProductionConfig")
