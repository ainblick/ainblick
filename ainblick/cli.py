import click
@click.command()
def hello():
  click.echo('Hello, World! This is ainblick test.')

if __name__ == '__main__':
  hello()