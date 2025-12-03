from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://akankshaojhainfo_db_user:onuIZ2BzLw5lMIE5@cluster0.fj5y0vb.mongodb.net/?appName=Cluster0")
db = client["todo_db"]
collection = db["items"]

@app.route('/todo')
def todo():
    return render_template('todo.html')


@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    data = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    collection.insert_one(data)

    return jsonify({"message": "To-Do Item Stored Successfully!"})
