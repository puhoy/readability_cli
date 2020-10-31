import click
import html2text

import requests
from readability import Document

@click.command()
@click.argument('url')
def cli(url):
    headers = {'User-Agent': 'readability_cli 0.1'}
    response = requests.get(url, headers=headers)
    doc = Document(response.text)
    click.echo(html2text.html2text(doc.summary()))

