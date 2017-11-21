import click
from facebook.login import Facebook


@click.command()
@click.option('--website', type=click.Choice(['facebook']), default='facebook')
def run(website):
    if website == 'facebook':
        facebook = Facebook()
        facebook.login()
    else:
        raise Exception("Website not found")


if __name__ == '__main__':
    run()
