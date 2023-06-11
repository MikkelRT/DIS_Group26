from flask import Flask, render_template, request
import psycopg2

app=Flask(__name__)

@app.route("/")
def index ():
    return render_template("index.html")

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="mikkelRT123"
)

@app.route("/success.html", methods=['GET', 'POST'])
def success():
    cartype = request.form['cartype']
    manufacturer = request.form['manufacturer']
    #model = request.form['model']
    #mileage = int(request.form['mileage'])
    #price = int(request.form['price'])
    #leatherseats = request.form['leatherseats']
    cur = conn.cursor()
    cur.execute('SELECT cartype, manufacturer, mileage, price FROM cars4sale WHERE manufacturer = %s AND cartype = %s;', (manufacturer, cartype))
    car = cur.fetchall() 
    return render_template("success.html", output=car)

@app.route("/index.html")
def goback():
    return render_template("index.html")


if __name__ == '__main__':
    app.debug=True
    app.run()
