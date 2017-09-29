from ldapdb.models.fields import CharField, IntegerField, ListField

import ldapdb.models


class LdapUser(ldapdb.models.Model):
     base_dn = "ou=people,dc=air-eisti,dc=fr"
     object_classes = ['inetOrgPerson']

     uid = CharField(db_column="uid", max_length=200, primary_key=True)
     commonname = CharField(db_column='cn', max_length=200)
     surname = CharField(db_column='sn', max_length=200)

     password = CharField(db_column='userPassword', max_length=200)

     mail = CharField(db_column='mail', max_length=200, unique=True)
     tel = CharField(db_column='telephoneNumber', max_length=20, default='')


     def __str__(self):
         return self.uid

     def __unicode__(self):
         return self.uid
