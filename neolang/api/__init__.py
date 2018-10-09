from flask import jsonify
from flask import Blueprint
from neolang.api.models import *

api = Blueprint('api', 'api', url_prefix='/v1')

@api.route('/types')
def entry_types():
  # parts = LanguagePart.query.all()
  # res = [{'id': p.id, 'name': p.name} for p in parts]
  return jsonify({})

