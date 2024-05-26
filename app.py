from flask import Flask
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.view_web import vista_usuarios 

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.register_blueprint(vista_usuarios.blueprint)

if __name__ == '__main__':
    app.run(debug=True)
