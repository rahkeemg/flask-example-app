"""
    This file is the main app.  
    Created as a means of quickly building and testing Flask application.

    Eventually, this file will be removed and the entry point of the application
    will be wsgi.py.  Until then this will remain.
"""
from application import app

if __name__ == '__main__':
    app.run(debug=True)