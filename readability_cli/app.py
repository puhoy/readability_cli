import click
from markdownify import markdownify as md

import requests
from readability import Document

@click.command()
@click.argument('url')
def cli(url):
    response = requests.get(url)
    doc = Document(response.text)
    click.echo(md(doc.summary()))

