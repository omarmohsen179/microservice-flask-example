from roles_modules.models import db
from flask import Flask, request, jsonify
from service import create_role
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/test1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/roles', methods=['POST'])
def create_role_api():
    return jsonify(create_role(request.json['name'])), 201
