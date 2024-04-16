
import requests
from flask import request, jsonify, Flask
from service import create_user, assign_role_to_user
from users_modules.models import db, User, Role, UserRoles
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/test1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/users', methods=['POST'])
def create_user_api():
    return jsonify(create_user(request.json['username'])), 201


@app.route('/users/<int:user_id>/roles', methods=['POST'])
def assign_role_to_user_api(user_id):
    return jsonify(assign_role_to_user(user_id, request.json['role_id'])), 201
