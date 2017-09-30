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
### RedHat/Fedora:
```
# yum install python-devel openldap-devel
```

## Python dependencies

Create virtualenv and activate it:
```
$ virtualenv -p python3 venv
(venv)$ source venv/bin/activate
```

Install dependencies:
```
(venv)$ pip install -r requirement.txt
```

# Run development server:
```
(venv)$ python manage.py runserver
```
