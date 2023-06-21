from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.controllers import *
from application.models import *

app = Flask(__name__)

# Routes
app.add_url_rule('/', view_func=home)
app.add_url_rule('/users', view_func=get_users, methods=['GET'])
app.add_url_rule('/users/<user_id>', view_func=get_user, methods=['GET'])
app.add_url_rule('/users', view_func=create_user, methods=['POST'])
app.add_url_rule('/users/<user_id>', view_func=update_user, methods=['PUT'])
app.add_url_rule('/users/<user_id>', view_func=delete_user, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
