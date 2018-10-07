from neolang import db

class LanguagePart(db.Model):
  __tablename__ = 'language_parts'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)

  def __init__(self, name):
    self.name = name
