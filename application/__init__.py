"""
    Flask Application Factory
    The layout of this application was taken from the following blog site:
    https://hackersandslackers.com/flask-application-factory/

    Another very useful resource can be found at the youtube link below.
    I found this one to be very informative in setting up the main
    application format and explaining the logic behind such a setup.
    https://youtu.be/44PvX0Yv368
"""

from flask import Flask

app = Flask(__name__)

from application import routes

## This section will be used to embed  sub applications 
## within the main flask application
# def create_app():

#     ## Initialize the core application ##
#     app = Flask(__name__, instance_relative_config=False)
#     app.config.from_object('config.Config')
    
#     ## Initialize pluggins in this section


#     with app.app_context():
#         # Include our Routes
#         from . import routes

#         # Register blueprints if they are used.

#         return app