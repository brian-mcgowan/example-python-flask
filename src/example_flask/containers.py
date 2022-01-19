import logging
import sys

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    logging = providers.Resource(
        logging.basicConfig,
        datefmt=config.logging.DATEFMT,
        format=config.logging.FORMAT,
        level=config.logging.LEVEL,
        stream=sys.stdout,
    )
