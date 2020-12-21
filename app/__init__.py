from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GrandPy'
from app import routes