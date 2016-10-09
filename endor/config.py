"""Read Configurations of environment."""
import os


def get_config():
    """."""
    config = {
        'DB_SECTION': os.getenv('DB_SECTION', 'sqlalchemy')
    }
    return config
