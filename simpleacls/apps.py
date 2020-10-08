from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError


class SimpleAclsConfig(AppConfig):
    name = 'simpleacls'

    def ready(self):
        super().ready()
        try:
            from simpleacls.acls import initialize

            initialize()
        except (OperationalError, ProgrammingError):
            pass  # running migrations
