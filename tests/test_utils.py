from django.test import TestCase
from coreapp.models import LdapUser, User
import coreapp.utils


class HashPasswordTestCase(TestCase):
    def test_hash_password(self):
        self.assertEqual('{SHA}PkEX3wXp71oONtMvdlHdq6AnSPM=', coreapp.utils.hash_password('plouf'))
        self.assertEqual('{SHA}6PyxUBps2qg0332JEJ9tFDrRtIo=', coreapp.utils.hash_password('plif'))


class ImportLdapUsersTestCase(TestCase):
    def test_import_ldap_users(self):
        LdapUser.objects.create(
            uid='toto',
            commonname='toto',
            surname='titi',
            password='pass',
            mail='mail',
            tel='0123456789'
        )

        coreapp.utils.import_ldap_users(LdapUser, User)
        user = User.objects.first()
        self.assertEqual(user.username, 'toto')
        self.assertEqual(user.first_name, 'toto')
        self.assertEqual(user.last_name, 'titi')
        self.assertEqual(user.password, 'pass')
        self.assertEqual(user.email, 'mail')
        self.assertEqual(user.tel, '0123456789')

    @classmethod
    def tearDownClass(cls):
        LdapUser.objects.all().delete()
        User.objects.all().delete()
        super(ImportLdapUsersTestCase, cls).tearDownClass()
