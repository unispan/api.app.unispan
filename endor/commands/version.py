"""information for version."""

import click
from endor.cli import pass_context


@click.command()
@pass_context
def command(context):
    """Show the API of app Unispan version information."""
    from endor import __version__
    from endor.api import __version__ as __version_api__
    context.log('API of APP Unispan:')
    context.log(' Version:      %s' % __version__)
    context.log(' API version:  %s' % __version_api__)
