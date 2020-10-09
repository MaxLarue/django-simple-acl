
class SimpleAclException(Exception):
    pass


class CouldNotLoadAclDefinition(SimpleAclException):
    def __init__(self, definition_path):
        super("""
Unable to load acl definition at path %s, make sure the module is correct and the object name exists 
""" % definition_path)


class CouldNotCreateGroup(SimpleAclException):
    def __init__(self, group_name, exception):
        super("""
An unexpected exception occurred while creating group %s.
Original exception was: %s
""" % (group_name, exception))


class GroupMissingForAclDefinition(SimpleAclException):
    def __int__(self, group_name):
        super("""
An acl definition was found with a group name that doesn't exist: %s.
Make sure it is declared in settings, or created by another way before simpleacls' initialization
""")


class PermissionMissingForAclDefinition(SimpleAclException):
    def __init__(self, model, group):
        super("""
Error while linking permission to group %s for model %s, make sure model is a concrete model class and that django auth
package is installed.        
""" % (model, group))