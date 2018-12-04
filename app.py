from flask import request, jsonify
from app.models import Call
from app import app, db
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/call/', methods=['POST'])
def save_call():
    if request.json:
        content = request.json
        new_call = Call(
            user_id=content.get('id', 0),
            call_type=content.get('type', 0),
            street=content.get('street', None),
            number=content.get('number', None),
            city=content.get('city', None),
            state=content.get('state', None),
            neighborhood=content.get('neighborhood', None),
            observation=content.get('observation', None),
            complement=content.get('complement', None),
            lat=content.get('lat', None),
            lng=content.get('lng', None)
        )
        db.session.add(new_call)
        db.session.commit()
    return 'Hello, World!'

@app.route('/call/<int:id>/', methods=['GET'])
def get_users_calls(id):
    calls = Call.query.filter_by(user_id=id).all()
    return jsonify([call.serialize for call in calls])


if __name__ == "__main__":
    db.create_all()
    app.run()