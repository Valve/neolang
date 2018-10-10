from neolang import db

class EntryType(db.Model):
  NOUN = 1
  VERB = 2

  __tablename__ = 'entry_types'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)

  def __init__(self, id, name):
    self.id = id
    self.name = name

class Entry(db.Model):
  __tablename__ = 'entries'

  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.Text, nullable=False)
  entry_type_id = db.Column(db.Integer, 
    db.ForeignKey('entry_types.id'),
    nullable=False)

  entry_type = db.relationship('EntryType', backref=db.backref('entries', lazy='dynamic'))
  translations = db.relationship('Translation', backref=db.backref('Entry'))
  examples = db.relationship('Example', backref=db.backref('Entry'))
  verb_tenses = db.relationship('VerbTense', backref=db.backref('Entry'))

  def __init__(self, id, text, entry_type_id):
    self.id = id
    self.text = text
    self.entry_type_id = entry_type_id


class Translation(db.Model):
  __tablename__ = 'translations'

  id = db.Column(db.Integer, primary_key=True)
  # https://www.w3schools.com/tags/ref_language_codes.asp
  lang = db.Column(db.String(2), nullable=False)
  entry_id = db.Column(db.Integer, 
    db.ForeignKey('entries.id'),
    nullable=False)
  translation = db.Column(db.Text, nullable=False)
  comment = db.Column(db.Text, nullable=True)

  entry = db.relationship('Entry', backref=db.backref('Translation', lazy='dynamic'))

  def __init__(self, entry, translation, lang='ka'):
    self.lang = lang
    self.entry = entry
    self.translation = translation



class Example(db.Model):
  __tablename__ = 'examples'

  id = db.Column(db.Integer, primary_key=True)
  entry_id = db.Column(db.Integer, 
    db.ForeignKey('entries.id'),
    nullable=False)
  example = db.Column(db.Text, nullable=False)
  translation = db.Column(db.Text, nullable=False)

  entry = db.relationship('Entry', backref=db.backref('Example', lazy='dynamic'))

  def __init__(self, entry, example, translation):
    self.entry = entry
    self.example = example
    self.translation = translation

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


  entry = db.relationship('Entry', backref=db.backref('VerbTense', lazy='dynamic'))

  def __init__(self, entry, time_reference, 
    first_singular, second_singular, third_singular,
    first_plural, second_plural, third_plural):
    self.entry = entry
    self.time_reference = time_reference
    self.first_singular = first_singular
    self.second_singular = second_singular
    self.third_singular = third_singular
    self.first_plural = first_plural
    self.second_plural = second_plural
    self.third_plural = third_plural


class Recording(db.Model):
  __tablename__ = 'recordings'

  id = db.Column(db.Integer, primary_key=True)
  entity_id = db.Column(db.Integer, nullable=False)
  entity_type = db.Column(db.Text, nullable=False)
  path = db.Column(db.Text, nullable=True)
