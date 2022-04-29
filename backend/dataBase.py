from flask import Flask, jsonify, Response, request, abort
from User import User
from pymongo import MongoClient
import pymongo

app = Flask(__name__)

def getDatabase():
    CONNECTION_STRING = "mongodb://user:ShopNet@localhost/admin"
    client = MongoClient(CONNECTION_STRING)
    return client

dataBase = getDatabase()["ShopNet"]
UserCollection = dataBase["users"]


users = [
    User("Alex", "Alba"),
    User("Ion", "Bucuresti")
    ]

@app.route('/api/users', methods = ['POST'])
def addUser():
    content = request.json
    user = User(content['nume'], content['oras'])
    UserCollection.insert_one(user.__dict__)
    return Response()


@app.route('/api/users/<id>', methods = ['GET'])
def getById(id):
    for i in users:
        if i.getId() == id:
            return i.__dict__  
    return Response('{"error" : "Not found any user}"', 404)
