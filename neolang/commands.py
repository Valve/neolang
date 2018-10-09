import click

@click.command(help="seeds the DB")
def seed():
  from neolang.api.models import Entry, EntryType, Translation, Example, VerbTense
  print(Entry().translations)
