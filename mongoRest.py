from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import json,urllib
import urllib.request
import re
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/playersDb'

mongo = PyMongo(app)
def getUrl():
  url ='https://alivebyacadomia.github.io/headtohead.json'
  f = urllib.request.urlopen(url)
  data = f.read()
  encoding = f.info().get_content_charset('utf-8')
  JSON_object = json.loads(data.decode(encoding))
  print(JSON_object['players'])
  mongo.db.drop_collection("players")
  player = mongo.db.players
  lenght = len(JSON_object['players'])
  print(lenght)
  for i in range(0,lenght):
    star_id = player.insert(JSON_object['players'][i])
  return "added"
@app.route('/players', methods=['GET'])
def get_all_players():
  getUrl()
  player = mongo.db.players
  output = []
  for s in player.find():
    output = {'id': s['id'], 'firstname': s['firstname'], 'lastname': s['lastname'], 'shortname': s['shortname'],'sex': s["sex"], 'country':s['country'], 'picture': s['picture'],'data': s['data']}
  return jsonify({'result' : output})


@app.route('/players/<int:id>', methods=['GET'])
def getById(id):
  getUrl()
  player = mongo.db.players
  s = player.find_one({'id' : id})
  if s:
    output = {'id': s['id'], 'firstname': s['firstname'], 'lastname': s['lastname'], 'shortname': s['shortname'],'sex': s["sex"], 'country':s['country'], 'picture': s['picture'],'data': s['data']}
  else:
    output = "No Data of this Id"
  return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(debug=True)
