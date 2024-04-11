from flask import Flask
from auth_modules.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5000)
# python -m venv venv
# .\venv\Scripts\activate
