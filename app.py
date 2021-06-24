from datetime import datetime
from flask import Flask,json, jsonify, request, render_template
from pgdb import connect

app= Flask(__name__)

#PostgreSQL connection
con= connect(dbname='geodb', host='localhost', port=5432, user='postgres', password='admin')
cursor = con.cursor()


@app.route('/')
def Index():
    cursor.execute(''' SELECT DISTINCT postal_code FROM paystats ''')
    postal_codes = cursor.fetchall()
    cursor.execute("SELECT DISTINCT p_age FROM paystats")
    ages = cursor.fetchall()
    return render_template('index.html', pcs=postal_codes, age_range =ages )
    
# Get all postal codes geometries
@app.route('/getAllPolygons')
def get_all_polygons():
    cursor.execute(''' SELECT ST_AsText(the_geom) FROM postal_codes ''')
    data=cursor.fetchall()
    return jsonify(data)

# Get total payment amount by postalcode, age and gender
@app.route('/getTotalAmount/postalcode_age_gender')
def get_total_amount_postalcode_age_gender():
    if request.method == "GET":
        cursor.execute(''' 
            SELECT postal_code, p_age, gender, sum(amount), count(id) as totalPeople
            FROM paystats 
            GROUP BY postal_code, p_age, gender
            ORDER BY postal_code, p_age, gender
        ''')
        data=cursor.fetchall()
        datadict=[{  "postal_code":d.postal_code,
                    "p_age":d.p_age,
                    "gender":d.gender,
                    "amount":d.sum,
                    "total_people":d.totalpeople
                } 
                for d in data]
        return jsonify({
                "message" : "All data",
                "data" : datadict})




# Obtain total payment amount by date
@app.route('/getTotalAmount/date', methods=["POST"])
def get_total_amount_date():
   if request.method == "POST":
       start_date = request.form['start_date']
       finish_date = request.form['finish_date']
       
       cursor.execute(''' SELECT SUM(amount) FROM paystats WHERE p_month BETWEEN %s AND %s ''',(start_date,finish_date))
       data=cursor.fetchall()
       return jsonify({
           "start_date":start_date,
           "finish_date":finish_date,
           "total_amount_by_date":data[0]
        })

# Obtain total payment amount by gender
@app.route('/getTotalAmount/gender', methods=["POST"])
def get_total_amount_gender():
    if request.method == "POST":
        gender= request.form['gender']
        cursor.execute(''' SELECT SUM(amount) from paystats WHERE gender=%s ''',(gender))
        data=cursor.fetchall()
        return jsonify({
            "gender":gender,    
            "total_amount_by_gender":data[0]
        })

# Obtain total payment amount by postal code
@app.route('/getTotalAmount/postal_code', methods=["POST"])
def get_total_amount_postal_code():
    if request.method == "POST":
        postal_code= request.form['postal_code']
        cursor.execute('''SELECT SUM(amount) from paystats WHERE postal_code={0}'''.format(postal_code))
        data=cursor.fetchall()
        return jsonify({
            "postal_code":postal_code,    
            "total_amount_by_postal_code":data[0]
        })

# Obtain total payment amount by age
@app.route('/getTotalAmount/age', methods=["POST"])
def get_total_amount_age():
    if request.method == "POST":
        age= request.form['age']
        str(age)
        cursor.execute(f''' SELECT SUM(amount) from paystats WHERE p_age = '{age}' ''')
        data=cursor.fetchall()
        return jsonify({
            "age":age,    
            "total_amount_by_age":data[0]
        })



if __name__ == '__main__':
    app.run(port=3000, debug=False)
    
cursor.close()
con.close
