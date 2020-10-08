import os
from django.urls import path
from django.contrib import admin
from testautoload.groups import DRIVER, SHOP_EMPLOYEE, SALESMAN, ACCOUNTANT, MANAGER

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ROOT_URLCONF = "djangoaclgroups.urls"

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    'simpleacls.apps.SimpleAclsConfig',
    "tests",
    "testautoload"
)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

SECRET_KEY = "secret_key_for_testing"

SIMPLE_ACLS = {
    "groups": [DRIVER, SHOP_EMPLOYEE, SALESMAN, ACCOUNTANT, MANAGER],
    "acls": [
        "testautoload.acls.ACLS"
    ]
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
