""" this module takes care of the run project flask """
import os
import sys

from app import app, logger

if __name__ == "__main__":

    if os.environ.get("DEBUG_FLASK") not in ['true', 'True', ''] or os.environ.get("DEBUG_FLASK") is None:
        logger.error("La variable DEBUG_FLASK n'est pas correct")
        sys.exit()
    if os.environ.get("SECRET_KEY") is None:
        logger.error("La variable SECRET_KEY n'est pas correct")
        sys.exit()
    if os.environ.get("key_api_google") is None:
        logger.error("La variable key_api_google n'est pas correct")
        sys.exit()

    debug = bool(os.environ.get("DEBUG_FLASK"))
    app.run(debug=debug)
