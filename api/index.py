from flask import Flask, render_template
from flask_mysql_connector import MySQL
import os

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

# DB config.
app.config["MYSQL_HOST"] = os.getenv('MYSQL_HOST')
app.config["MYSQL_USER"] = os.getenv('MYSQL_USER')
app.config["MYSQL_PASSWORD"] = os.getenv('MYSQL_PASSWORD')
app.config["MYSQL_DATABASE"] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT'))

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')