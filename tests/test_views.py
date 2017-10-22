from django.test import TestCase
from django.test import Client
from coreapp.models import LdapUser
from coreapp.utils import hash_password


class UserViewTestCase(TestCase):
    user_post = {'uid': 'toto',
                'commonname': 'toto',
                'surname': 'titi',
                'mail': 'toto@titi.com',
                'password': 'plouf'}
    user_get = {'uid': 'toto',
                'commonname': 'toto',
                'surname': 'titi',
                'mail': 'toto@titi.com',
                'tel': ''}

    def test_add_user(self):
        response = self.client.post('/users/', self.user_post)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), self.user_get)

    def test_get_user(self):
        response = self.client.get('/users/toto/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.user_get)

    def test_update_user_password(self):
        response = self.client.patch('/users/toto/',
                                     data='{"password": "plif"}',
                                     content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.user_get)
        self.assertEqual(LdapUser.objects.get(uid='toto').password, hash_password('plif'))

    def test_get_all_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.user_get])

    def test_search_user(self):
        response = self.client.get('/users/?q=tot')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.user_get])

    @classmethod
    def tearDownClass(cls):
        LdapUser.objects.all().delete()
        super(UserViewTestCase, cls).tearDownClass()
