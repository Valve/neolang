from flask import jsonify
from flask import Blueprint
from sqlalchemy.orm import selectinload
from neolang.api.models import *

api = Blueprint('api', 'api', url_prefix='/v1')

@api.route('/entries', methods=['GET'])
def entries():
  entries = Entry.query.options(selectinload(Entry.translations)).all()
  res = []
  for e in entries:
    res.append({
      'id': e.id, 
      'entry': e.text, 
      'translation': e.translations[0].translation})

  return jsonify(res)

@api.route('/entries/<int:id>', methods=['GET'])
def entry(id):
  entry = Entry.query.get(id)
  res = {
    'id': entry.id,
    'text': entry.text
  }
  if entry.translations:
    res['translation'] = entry.translations[0].translation
  if entry.examples:
    res['example'] = {
      'example': entry.examples[0].example,
      'translation': entry.examples[0].translation
    }
  return jsonify(res)



