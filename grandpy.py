import os

from app import app

if __name__ == "__main__":
    debug = bool(os.environ.get('DEBUG'))
    app.run(debug=True)