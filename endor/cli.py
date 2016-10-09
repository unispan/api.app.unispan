"""."""
# -*- coding: utf-8 -*-
import os
import sys
import click
import yaml

CONTEXT_SETTINGS = dict(auto_envvar_prefix='ENDOR')


class Context(object):
    """Context API."""

    def __init__(self):
        """Initial configuration."""
        self.verbose = False
        self.config = {}
        self.session = None
        self.backingServices = {}

    def read_config(self, filename):
        """Read configuration."""
        with open(filename, 'r') as f:
            self.config = yaml.load(f)

    def log(self, msg, *args):
        """Write logs message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Write logs message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(
                    os.path.join(os.path.dirname(__file__), 'commands'))


class EndorCLI(click.MultiCommand):
    """."""

    def list_commands(self, ctx):
        """List commands."""
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename[:-3] != '__init__':
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """Read commands."""
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('endor.commands.' + name,
                             None, None, ['command'])
        except ImportError:
            return
        return mod.command


def read_config(context, param, value):
    """Read configuration.

    Callback that is used whenever --config is passed.We use this to
    always load the correct config.  This means that the config is loaded
    even if the group itself never executes so our aliases stay always
    available.
    """
    cfg = context.ensure_object(Context)
    if value is None:
        value = os.path.join(
                os.path.dirname(__file__), '..', 'endor.yaml')
    cfg.read_config(value)
    return value


@click.option('--config', envvar='CONFIG',
              type=click.Path(exists=True, dir_okay=True),
              callback=read_config, expose_value=True,
              help='The config file to use instead of the default.')
@click.command(cls=EndorCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@pass_context
def cli(context, verbose, config):
    """A complex command line interface."""
    context.verbose = verbose
