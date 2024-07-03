from flask_mysqldb import MySQL

from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'database'


mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def index():
    cur = mysql.connection.cursor()
    res = cur.execute('''select * from applications where Title like "Новая" order by DateAdd desc''')
    if res > 0:
        details = cur.fetchall()
        return render_template('home.html', details=details)

@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html')
 
@app.route('/zayavka')
def zayavka():
    cur = mysql.connection.cursor()
    res = cur.execute('''select * from applications order by DateAdd desc''')
    if res > 0:
        details = cur.fetchall()
        return render_template('zajavka.html', details=details)

@app.route('/question')
def question():
    cur = mysql.connection.cursor()
    res = cur.execute('''select IdQuestion, FIO, Phone, Descriptions from questions''')
    if res > 0:
        details = cur.fetchall()
        return render_template('question.html', details=details)


if __name__ == '__main__':
    app.run(debug=True)