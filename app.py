from flask import Flask

app  = Flask(
            __name__, 
            static_folder="static/",
             template_folder="templates/",
            )

from routes.routes import *
from api.algorithms_api import *

if __name__ == "__main__":
    app.debug = True
    