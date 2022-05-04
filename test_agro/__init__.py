"""Main entry point
"""
from pyramid.config import Configurator
from test_agro.data.db_session import DbSession


def main(global_config, **settings):
    config = Configurator(settings=settings)
    init_db(config)
    config.include("cornice")
    config.scan("test_agro.api_customer")
    config.scan("test_agro.api_product")
    config.scan("test_agro.api_order")

    return config.make_wsgi_app()

def init_db(_):
    DbSession.global_init()

