import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
]

DATABASES = {
    'ldap': {
        'ENGINE': 'ldapdb.backends.ldap',
        'NAME': 'ldap://172.17.4.164/',
        'USER': 'uid=admin,ou=people,dc=air-eisti,dc=fr',
        'PASSWORD': 'admin',
    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASE_ROUTERS = ['ldapdb.router.Router']
