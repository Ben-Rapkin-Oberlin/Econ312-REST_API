# app.py
from flask import Flask, request, jsonify
from flask import Flask, render_template

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]



@app.get("/")
def get_countries():
    return jsonify(countries)


@app.delete("/")
def delete_country():
    if request.is_json:
        a=request.get_json()
        print(a)
        print(a["id"])
        #print(len(countries))
        countries.pop(a["id"]-1)

        return a, 201
    return {"error": "Request must be JSON"}, 415

@app.route('/')
def home():
    
    return render_template("home.html", countries=jsonify(countries))
