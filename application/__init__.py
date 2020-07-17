from flask import Flask

"""
    Flask Application Factory
    The layout of this application was taken from the following blog site:
    https://hackersandslackers.com/flask-application-factory/
"""

def create_app():

    ## Initialize the core application ##
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    ## Initialize pluggins in this section


    with app.app_context():
        # Include our Routes
        from . import routes

        # Register blueprints if they are used.

        return app