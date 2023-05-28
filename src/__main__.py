from app import application
import os
from wsgiref.simple_server import make_server

if __name__ == "__main__":
	if os.getenv("ENV") == "DEVELOPMENT":
		application.run(host="0.0.0.0", debug=False)
	application.run(host="0.0.0.0", debug=False)
