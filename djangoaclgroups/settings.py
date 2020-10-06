INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    'aclgroups',
    "tests"
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
SECRET_KEY = "secret_key_for_testing"