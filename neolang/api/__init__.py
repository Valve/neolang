from flask import jsonify
from flask import Blueprint
from neolang.api.models import LanguagePart

api = Blueprint('api', 'api', url_prefix='/api')

@api.route('/parts')
def language_parts():
  parts = LanguagePart.query.all()
  res = [{'id': p.id, 'name': p.name} for p in parts]
  return jsonify(res)
