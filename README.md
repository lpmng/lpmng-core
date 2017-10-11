# lpmng-core
Core for the next generation LAN party manager

# Installation

Clone project and cd into it

## System dependencies
You will need openldap library:

### Debian/Ubuntu:

```
# apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```
TODO: test if it needs other package for python 3

### RedHat/Fedora:
```
# yum/dnf install python3-devel openldap-devel
```

## Python dependencies

Create virtualenv and activate it:
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Install dependencies:
```
(venv)$ pip install -r requirement.txt
```

# Run development server:
```
(venv)$ python manage.py runserver
```
