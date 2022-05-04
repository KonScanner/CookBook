import click


@click.command()
@click.option('--string', default='World', help='This is the thing that is greeted.')
@click.option('--repeat', default=1, help='How many times you should be greeted! ')
@click.argument('out', type=click.File('w'), default='-', required=False)
def say(string, repeat, out):
    """This script greets you!"""
    # out.write('test\n')
    for _ in range(repeat):
        click.echo(f'Hello {string}!', file=out)


say()
