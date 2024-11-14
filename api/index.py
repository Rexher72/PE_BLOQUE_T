from flask import Flask, render_template, session, request
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
    if not session["done"]:
        return render_template('index.html')
    else:
        return render_template('message.html')

@app.route('/edad') 
def age():
    if not session["done"]:
        return render_template('page1.html')
    else:
        return render_template('message.html')

@app.route('/genero', methods=['POST'])
def gender():
    if request.method == 'POST':
        if not session["done"]:
            session["age"] = request.form.get("age")
            return render_template('page2.html')
        else:
            return render_template('message.html')

@app.route('/register-time', methods=['POST'])
def registerTime():
    if request.method == 'POST':
        if not session["done"]:
            _time = request.form.get("time")
            _gender = request.form.get("gender")
            _age = session["age"]
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO times VALUES (%s, %s)", (_time, _gender, _age))
            mysql.connection.commit()
            session["done"] = True
            return "OK"
