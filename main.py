# #here we are import in the moduls
from typing import Dict

from flask import Flask, jsonify, render_template, request
import mongodb
from pymongo import MongoClient

# here we create a object from Flask class
Rest_Api_app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://patrik1003:Super_Secret-007@cluster0.q68jswv.mongodb.net/?retryWrites=true&w=majority")

mydb = client['mydatabase']


@Rest_Api_app.route("/users", methods=["GET"])
def get_users_function():
    return jsonify({"name": " Patrik Polgar "})


@Rest_Api_app.route("/questions", methods=["POST"])
def save_question_function():
    collection_name = mydb["Questions"]
    my_question = {"_id": 1, "name" : "Patrik Polgar"}
    collection_name.insert_one(my_question)
    return my_question


Rest_Api_app.run(port=8080, debug=True)
