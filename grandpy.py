import os

from app import app

if __name__ == "__main__":
    debug = bool(os.environ.get('DEBUG_FLASK'))
    app.run(debug=debug)