from neolang import db

class EntryType(db.Model):
  __tablename__ = 'entry_types'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)

  def __init__(self, name):
    self.name = name

class Entry(db.Model):
  __tablename__ = 'entries'

  id = db.Column(db.Integer, primary_key=True)
  lang = db.Column(db.String(2), nullable=False)
  word = db.Column(db.Text, nullable=False)
  entry_type_id = db.Column(db.Integer, 
    db.ForeignKey('entry_types.id'),
    nullable=False)

  entry_type = db.relationship('EntryType', backref=db.backref('entries', lazy='dynamic'))
  translations = db.relationship('Translation', backref=db.backref('Entry'))
  examples = db.relationship('Example', backref=db.backref('Entry'))

class Translation(db.Model):
  __tablename__ = 'translations'

  id = db.Column(db.Integer, primary_key=True)
  entry_id = db.Column(db.Integer, 
    db.ForeignKey('entries.id'),
    nullable=False)
  translation = db.Column(db.Text, nullable=False)
  comment = db.Column(db.Text, nullable=True)

  entry = db.relationship('Entry', backref=db.backref('Translation', lazy='dynamic'))



class Example(db.Model):
  __tablename__ = 'examples'

  id = db.Column(db.Integer, primary_key=True)
  entry_id = db.Column(db.Integer, 
    db.ForeignKey('entries.id'),
    nullable=False)
  example = db.Column(db.Text, nullable=False)
  translation = db.Column(db.Text, nullable=False)

  entry = db.relationship('Entry', backref=db.backref('Example', lazy='dynamic'))

class VerbTense(db.Model):
  __tablename__ = 'verb_tenses'

  id = db.Column(db.Integer, primary_key=True)
  time_reference = db.Column(db.Text, nullable=False)
  entry_id = db.Column(db.Integer, 
    db.ForeignKey('entries.id'),
    nullable=False)
  first_singular = db.Column(db.Text, nullable=False)
  second_singular = db.Column(db.Text, nullable=False)
  third_singular = db.Column(db.Text, nullable=False)
  first_plural = db.Column(db.Text, nullable=False)
  second_plural = db.Column(db.Text, nullable=False)
  third_plural = db.Column(db.Text, nullable=False)

  entry = db.relationship('Entry', backref=db.backref('verb_tenses', lazy='dynamic'))

class Recording(db.Model):
  __tablename__ = 'recordings'

  id = db.Column(db.Integer, primary_key=True)
  entity_id = db.Column(db.Integer, nullable=False)
  entity_type = db.Column(db.Text, nullable=False)
  path = db.Column(db.Text, nullable=True)
