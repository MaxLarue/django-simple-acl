============
django-simple-acl
============

Configuring builtin groups and permissions declaratively from code as static access control lists. Integrates with
 django built-in model permissions

Features:

- Define a list of groups that should exist at all time
- Bind to each group a set of crud permissions to any model


Summary
============

    - installation :ref:`_install`
    - configuration :ref:`_config`
    - usage :ref:`_usage`
    - gotchas :ref:`_gotchas`
    - testing :ref:`_testing`
    - rest framework :ref:`_drf`

.. _install:

Installation
============

#. `pip install django-groups-acl`
#. Add `'simpleacls'` to `INSTALLED_APPS`

.. _config:

Configuration
=============

.. code-block:: python

    SIMPLE_ACLS = {
        groups: [
            "admin",
            "moderator",
            "reader",
            "gremlins"
        ],
        acls: [
            "library.permissions.ACLS",
            "swimmingpool.permissions.ACLS",
            "polls.permissions.ACLS",
            "myproject.permissions.ACLS",
        ]
    }

.. _usage:

Usage
=====

With django-simple-acls you define the groups of users you need in your app, which CRUD permission each group brings to
the user and on application startup the groups are created and model permissions are linked.

Everything happens at startup and the final state is dictated by your code, which makes it simple to configure, update
and replicate in multiple deployments.

To setup django-simple-acls, you must define a SIMPLE_ACL dictionary inside your settings.py file. Entries are:
    - groups: a list of string representing the groups names
    - acls: a list of path to the acls objects

`acls` is a list of path such as those of middleware in the form "path.to.module.objectinsidethemodule". The goal here
is to have acls live inside the same module as the model they apply on.

An example SIMPLE_ACL config can be found inside the test source:

.. code-block:: python

    SIMPLE_ACLS = {
        "groups": [DRIVER, SHOP_EMPLOYEE, SALESMAN, ACCOUNTANT, MANAGER],
        "acls": [
            "testautoload.acls.ACLS"
        ]
    }

where DRIVER, SHOP_EMPLOYEE, SALESMAN, ACCOUNTANT and MANAGER are actually the group name (as a string).

The acl declaration structure in itself can be as follow:

.. code-block:: python

    from myapp.models import MyCoolModel
    from myapp.groups import ANONYMOUS, USER, ADMIN
    from simpleacls.acls import C, R, U, D

    ACLS = {
        MyCoolModel: {
            ANONYMOUS: {R}
            USER: {C, R, U},
            ADMIN: {C, R, U, D}
        }
    }

In other words, acl declarations are a mapping of models, to groups, to permissions.

C, R, U, D are create, read, update delete permissions on a certain model.

The model itself is the key in the ACLS mapping (not his name, the actual model class).

On this model we define a map of groups and for each groups, which permission is available.

Permissions are a set of C, R, U, D.

The group key is actually the group name (if you have a group called admin, it would be 'admin'). But you'll probably
want to maje these constants in your project or an enum.

If you omit a group for a model, that group will have no permission on that model.

If you define two sets of permissions for the same group, on the same model, they will be merged and duplicates removed.
(meaning if you define two sets of permission, the resulting permission set will be the highest combination of both)

.. _gotchas:

Gotchas
=====

If you omit the SIMPLE_ACLS settings or make a typo in the name, no permission will be loaded

If you need to define an empty set of permissions use `set()` as `{}` is an empty dictionary.

If the acl path in SIMPLE_ACLS["acl"] is not valid (module does not exist or does not have the specified object). Then
your application won't start (but you should see a warning about it).

In other for permissions to be loaded inside your tests, you need to use the AclTestMixin (see the test section
for detail).

.. _testing:

Testing
=====

The groups and permissions might not be setup correctly during your test (but they will be on application start). To
avoid confusion, and make sure everything is setup correctly, you should use the AclTestMixin in your integration/end2end
tests. Here is an example how to:

.. code-block:: python

    from django.test import TestCase
    from simpleacls.testutils import AclTestMxin

    class MyTest(AclTestMixin, TestCase):

        def test_something(self):
            some = Group.objects.get(name="some_groups")  # this group and it's permissions were created

.. _drf:

Usage with rest framework
=====

The fact permissions used are the django's models one makes it possible to use this package with any other package that
integrate with those. As an example to leverage these permissions on a drf viewset, you'd use the DjangoModelPermissions
class and you're set:

.. code-block:: python

    from rest_framework import viewsets
    from rest_framework.permissions import DjangoModelPermissions
    from myapp.models import MyCoolModel
    from myapp.serializers import MyCoolModelSerializer

    class CoolModelViewSet(viewsets.ModelViewSet):
        queryset = MyCoolModel.objects.all()
        serializer_class = MyCoolModelSerializer
        permission_classes = [DjangoModelPermissions]


This viewset will respect your acls, as the permissions live inside the database and are created upon startup.
