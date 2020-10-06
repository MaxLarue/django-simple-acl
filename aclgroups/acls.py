import django.apps
from collections import defaultdict
from django.contrib.auth.models import Group, Permission


class AclFlag:
    """Describe a permission to be tied to an existing group
    for a particular model.
    """
    def __init__(self, full_name):
        self.full_name = full_name

    def get_permission_code(self, model_name):
        return self.full_name

    def __repr__(self):
        return self.full_name


class BuiltinAclFlag(AclFlag):
    """Variation of acl flag that maps to builtin
    permissions
    """
    def __init__(self, code_partial, full_name):
        super().__init__(full_name)
        self.code_partial = code_partial

    def get_permission_code(self, model_name):
        return self.code_partial % model_name


C = BuiltinAclFlag("add_%s", "create")
R = BuiltinAclFlag("view_%s", "read")
U = BuiltinAclFlag("change_%s", "update")
D = BuiltinAclFlag("delete_%s", "delete")


def create_groups(groups):
    """Given a list of group name, creates them
    if they do not exist yet
    """
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)


def set_models_acl(acl_list):
    """Given a list of acls definitions, bind the appropriate permissions
    to the right group
    """
    groups = defaultdict(lambda: defaultdict(set))
    for acl in acl_list:
        for model in acl:
            for group_name, group_acl in acl[model].items():
                groups[group_name][model] |= group_acl
    for group_name, group_acls in groups.items():
        permission_names = set()
        for model, model_acls in group_acls.items():
            model_name = model._meta.model_name
            permission_names |= {
                f.get_permission_code(model_name) for f in model_acls
            }
        permissions = Permission.objects.filter(codename__in=permission_names)
        group = Group.objects.get(name=group_name)
        group.permissions.set(permissions)
