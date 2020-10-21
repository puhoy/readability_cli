import click
import html2text

import requests
from readability import Document

@click.command()
@click.argument('url')
def cli(url):
    response = requests.get(url)
    doc = Document(response.text)
    click.echo(html2text.html2text(doc.summary()))

