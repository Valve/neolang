from flask import jsonify
from flask import Blueprint
from neolang.api.models import *

api = Blueprint('api', 'api', url_prefix='/v1')

@api.route('/entries')
def entries():
  entries = Entry.query.all()
  res = []
  for e in entries:
    res.append({
      'id': e.id, 
      'entry': e.text, 
      'translation': e.translations[0].translation})

  return jsonify(res)

