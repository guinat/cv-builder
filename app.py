from flask import Flask
from modules.views import app_views
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
bcrypt = Bcrypt(app)

app.register_blueprint(app_views)

if __name__ == '__main__':
    app.run(debug=True)
