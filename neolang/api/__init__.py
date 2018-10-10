from flask import jsonify
from flask import Blueprint
from sqlalchemy.orm import selectinload
from neolang.api.models import *

api = Blueprint('api', 'api', url_prefix='/v1')

@api.route('/entries')
def entries():
  entries = Entry.query.options(selectinload(Entry.translations)).all()
  res = []
  for e in entries:
    res.append({
      'id': e.id, 
      'entry': e.text, 
      'translation': e.translations[0].translation})

  return jsonify(res)

