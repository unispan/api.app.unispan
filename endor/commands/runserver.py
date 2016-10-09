import click
from endor.cli import pass_context


@click.command()
@click.option('--host', default='127.0.0.1')
@click.option('--port', default=8000)
@pass_context
def command(context, host, port):
    """Run Server."""
    context.log('Serving on http://%s:%s' % (host, port))

    from endor.api.app import App
    from waitress import serve

    # Api instances are callable WSGI apps
    wsgiapp = App(context=context).api
    if host is None:
        host = context.config.server.host

    if port is None:
        port = context.config.server.port

    serve(wsgiapp, host=host, port=port)
