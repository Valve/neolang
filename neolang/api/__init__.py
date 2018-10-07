from flask import Blueprint
from neolang.api.models import LanguagePart

api = Blueprint('api', 'api', url_prefix='/api')

@api.route('/parts')
def language_parts():
  parts = LanguagePart.query.all()
