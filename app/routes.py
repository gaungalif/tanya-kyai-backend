from app import app, response
from app.controller import UserController
from app.controller import TanyaController
from app.controller import PostController
from flask import request
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin

@app.route('/')
@cross_origin()
def index():
    return 'Hello Flask Ahoy'

#create post app route
@app.route('/posts', methods=['GET'])
@cross_origin()
def PostList():
    return PostController.PostList()

@app.route('/posts/<id>', methods=['GET'])
@cross_origin()
def PostbyID(id):
    return PostController.PostbyID(id)

@app.route('/questions', methods=['GET'])
@cross_origin()
def TanyaList():
    return TanyaController.TanyaList()

@app.route('/questions/<id>', methods=['GET'])
@cross_origin()
def TanyabyID(id):
    return TanyaController.TanyabyID(id)