from app import app, response
from app.controller import UserController
from app.controller import TanyaController
from app.controller import PostController
from flask import request
from flask import jsonify
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
from flask_cors import cross_origin

@app.route('/')
@cross_origin()
def index():
    return 'Hello Flask Ahoy'

#create post app route
@app.route('/posts', methods=['GET', 'POST'])
# @cross_origin()
def Posts():
    if request.method == 'GET':
        return PostController.PostList()
    else:
        return PostController.PostAdd()

    
@app.route('/posts/<id>', methods=['GET', 'DELETE'])
# @cross_origin()
def PostbyID(id):
    if request.method == 'GET':
        return PostController.PostbyID(id)
    else:
        return PostController.PostDelete(id)


@app.route('/questions', methods=['GET', 'POST'])
# @cross_origin()
def Tanyas():
    if request.method == 'GET':
        return TanyaController.TanyaList()
    elif request.method == 'POST':
        return TanyaController.TanyaAdd()


@app.route('/questions/<id>', methods=['GET'])
# @cross_origin()
def TanyabyID(id):
    return TanyaController.TanyabyID(id)

@app.route('/file-upload', methods=['POST'])
def uploads():
    return UserController.upload()

