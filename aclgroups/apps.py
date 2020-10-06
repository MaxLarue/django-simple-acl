from django.conf import settings
from django.apps import AppConfig
from django.db.utils import OperationalError
from aclgroups.acls import create_groups, set_models_acl


class AclgroupsConfig(AppConfig):
    name = 'aclgroups'

    def ready(self):
        super().ready()
        try:
            from aclgroups.acls import set_models_acl
            
            groups = []
            acls = []

            if hasattr(settings, "ACL_GROUPS"):
                acl_settings = getattr(settings, "ACL_GROUPS"):
                groups = getattr(acl_settings, "GROUPS", [])
                acls = getattr(acl_settings, "ACL_DEFINITIONS", [])

            create_groups(groups)
            set_models_acl(acls)
        except OperationalError:
            pass  # running migrations