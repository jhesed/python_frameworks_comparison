"""
    gunicorn Web Server Gateway Interface

    :Author: Jhesed Tacadena
    :Date: 2017-06-14
"""

# ------------------------------------------------------------------------------
# SECTION :: Imports
# ------------------------------------------------------------------------------

from flask_restful_api import app as flask_app
import argparse

# ------------------------------------------------------------------------------
# SECTION :: Static Variables
# ------------------------------------------------------------------------------

app_factory = {
    'flask': flask_app
}


# ------------------------------------------------------------------------------
# SECTION :: Main
# ------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----- Retrieve app to run -----
    parser = argparse.ArgumentParser(
        description='Wraps applications in gunicorn WSGI')
    parser.add_argument('--app', type=str, default='flask',
                        help='Determines which app to run')
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=str, default=5000)
    args = parser.parse_args()

    # ----- Run the app -----
    app_factory[args.app].run(host=args.host, port=args.port)
