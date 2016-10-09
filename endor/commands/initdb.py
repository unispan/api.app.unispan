import click
from endor.config import get_config
from endor.cli import pass_context
from endor.api import models


@click.command()
@pass_context
def command(context):
    """Initialize the database."""
    db_section = None
    try:
        print get_config()
        DB_SECTION = get_config()['DB_SECTION']
        bs_section = context.config['backingServices'][DB_SECTION]

        context.log('Initialized the database')
        models.init_model(bs_section)
        context.log('Creanting database')
        models.start(bs_section)
        models.Base.metadata.create_all(models._engine_from_config(bs_section))
        models.commit()
        models.clear()
        context.log('Finally creation database')
    except:
        context.log('No exists Configurations for {}'.format(DB_SECTION))
