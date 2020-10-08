============
django-simple-acl
============

Configuring builtin groups and permissions declaratively from code as static access control lists

Features:

- Define a list of groups that should exist at all time
- Bind to each group a set of crud permissions to any model

Installation
============

#. `pip install django-groups-acl`
#. Add `'simpleacls'` to `INSTALLED_APPS`

Configuration
=============

.. code-block:: python

    ACL_GROUPS = {
        GROUPS: [
            "admin",
            "moderator",
            "reader",
            "gremlins"
        ],
        ACL_DEFINITIONS: [
            "library.permissions.ACLS",
            "swimmingpool.permissions.ACLS",
            "polls.permissions.ACLS",
            "myproject.permissions.ACLS",
        ]
    }


Usage
=====

Only if no RTFD documentation supplied 
