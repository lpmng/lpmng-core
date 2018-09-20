[![Build Status](https://travis-ci.org/lpmng/lpmng-core.svg?branch=master)](https://travis-ci.org/lpmng/lpmng-core)
[![Coverage Status](https://coveralls.io/repos/github/lpmng/lpmng-core/badge.svg?branch=master)](https://coveralls.io/github/lpmng/lpmng-core?branch=master)

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

### Opensuse:
```
# zypper install python3-devel openldap2 openldap2-devel
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
