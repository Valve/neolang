import os
import click
import requests
from flask.cli import with_appcontext
from neolang import db

@click.command()
@with_appcontext
def seed_entry_types():
  from neolang.api.models import Entry, EntryType, Translation, Example, VerbTense
  print('Seeding entry types')
  entry_type_values = [
    (EntryType.NOUN, 'Noun'),
    (EntryType.VERB, 'Verb'),
    (3, 'Adjective'),
    (4, 'Adverb'),
    (5, 'Pronoun'),
    (6, 'Preposition'),
    (7, 'Conjunction'),
    (8, 'Interjection'),
    (9, 'Expression'),
    (10, 'Proverb')
  ]
  for id, name in entry_type_values:
    db.session.add(EntryType(id=id, name=name))
  db.session.commit()
  print("Done seeding entry types")
  

@click.command(help="seeds the DB")
@with_appcontext
def seed():
  print('seeding')
  csv_url = os.environ['NEOLANG_SEED_CSV_URL']
  import requests
  import csv
  from io import StringIO
  from neolang.api.models import Entry, EntryType, Translation, Example, VerbTense

  res = requests.get(csv_url)
  csv_reader = csv.reader(StringIO(res.text))
  next(csv_reader) # skip headers
  for line in csv_reader:
    entry = Entry(
      id = int(line[0]),
      entry_type_id = EntryType.VERB,
      text = line[2]
    )
    translation = Translation(
      entry = entry,
      translation = line[3]
    )

    entry.translation = translation
    verb_tense = VerbTense(
      entry = entry,
      time_reference='present',
      first_singular=line[4],
      second_singular=line[5],
      third_singular=line[6],
      first_plural=line[7],
      second_plural=line[8],
      third_plural=line[9]
    )
    entry.verb_tense = verb_tense

    example = Example(
      entry = entry,
      example = line[-1],
      translation = line[-2]
    )
    entry.example = example

    db.session.add(entry)
  db.session.commit()
