import json
from flask import Flask,jsonify, request
app=Flask(__name__)

tasks=[
    {
        'id':1,
        'contact':"9987944456",
        'name':"Raju",
        'done':False
    },
    {
        'id':2,
        'contact':"9876543222",
        'name':u"Rahul",
        'done':False
    }
]

@app.route("/add-data", methods=["POST"]) 
def add_task(): 
    if not request.json: 
        return jsonify({ 
            "status":"error", 
            "message": "Please provide the data!" 
            },400) 
    contact=[
    {
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
]
    tasks.append(contact) 
    return jsonify({ 
        "status":"success", 
        "message": "Task added succesfully!" 
        })

if(__name__ == "__main__"):
    app.run(debug=True)