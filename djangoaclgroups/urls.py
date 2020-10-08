"""checklybackend URL Configuration

checkly mainly uses api views.
These always follow the same pattern,
which is one of:
    /api/{model name}/                list all records of type {model}
    /api/{model name}/{pk}            details of record of type {model} with pk {pk}
    /api/{model name}/{extra action}  defined on a model viewset basis, eg: login

Other urls include:
    - admin: the admin panel urls, required to enjoy admin panel
    - ping: a simple healthcheck, can be used for debugging / monitoring
    - auth: urls needed to use the API explorer against authentication protected endpoints
    when in debug mode.

When in debug mode, you can access the api explore (nice for quick manual test), by going to
/api
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
