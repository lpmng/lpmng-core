#!/bin/sh
set -e

# Create database directory
mkdir /tmp/ldap_db

# Start sldap
slapd -h ldap://127.0.0.1:3890 -f tests/fixtures/ldap/slapd.conf
# Be sure that sldap is started
sleep 1
# Add test data
ldapadd -H ldap://127.0.0.1:3890 -x -D 'uid=admin,ou=people,dc=air-eisti,dc=fr' -w admin -f tests/fixtures/ldap/ldap.ldif
