import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


from controllers.foods import addStudent, delStudent, getStudent, updateStudent
import models.foods


from utils.db import connectdb


app = Flask(__name__)


# sql config
app.config['SQLALCHEMY_DATABASE_URI'] = connectdb()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


CORS(app)


@app.errorhandler(404)
def error(e):
  return jsonify({
      'status': 404,
      'message': str(e).split(':')[0]
  })


@app.route('/')
def welcome():
  return jsonify({
      'status': 200,
      'message': 'Welcome to API'
  })


@app.post('/add-student')
def add():
  if request.method == 'POST':
    return addStudent()


@app.get('/get-student')
def get():
  return getStudent()


@app.delete('/del-student/<id>')
def delete(id):
  return delStudent(id)


@app.put('/put-student/<id>')
def update(id):
  return updateStudent(id)


# port
if __name__ == '__main__':
  app.run(debug=True, port=2003, host='0.0.0.0')
