from flask import Flask, render_template, session, request, redirect
from flask_mysql_connector import MySQL
import os

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')


# DB config.
"""app.config["MYSQL_HOST"] = os.getenv('MYSQL_HOST')
app.config["MYSQL_USER"] = os.getenv('MYSQL_USER')
app.config["MYSQL_PASSWORD"] = os.getenv('MYSQL_PASSWORD')
app.config["MYSQL_DATABASE"] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT'))"""

# mysql = MySQL(app)

@app.before_request
def setup():
    session.permanent = True

@app.route('/')
def home():
    if session.get("done") is None:
        return render_template('index.html')
    else:
        return render_template('message.html')

@app.route('/edad') 
def age():
    if session.get("done") is None:
        return render_template('page1.html')
    else:
        return render_template('message.html')

@app.route('/genero')
def gender():
    if session.get("done") is None:
        return render_template('page2.html')
    else:
        return render_template('message.html')
    
@app.route('/encuesta')
def encuesta():
    if session.get("done") is None:
        return render_template('page3.html')
    else:
        return render_template('message.html')

@app.route('/register-time', methods=['POST'])
def registerTime():
    if request.method == 'POST':
        if session.get("done") is None:
            _time = round(float(request.form.get("time"))/1000, 3)
            _gender = request.form.get("gender")
            _age = request.form.get("age")
            charGender = "X"
            if _gender == "Hombre":
                charGender = "H"
            elif _gender == "Mujer":
                charGender = "M"
            elif _gender == "Otro":
                charGender = "O"
            """cur = mysql.connection.cursor()
            cur.execute("INSERT INTO times (time, gender, age, moment) VALUES (%s, %s, %s, DATE_ADD(CURRENT_TIMESTAMP, INTERVAL 1 HOUR))", (_time, charGender, _age))
            mysql.connection.commit()"""
            session["done"] = True
            return "OK", 200
        
@app.route("/final")
def final():
    return render_template("message.html");
        
@app.route("/clear-session")
def clear_session():
    session.clear()
    return "Cleared!"
