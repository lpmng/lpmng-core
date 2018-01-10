from django.test import TestCase
from django.test import Client
from coreapp.models import User


class UserViewTestCase(TestCase):
    user_post = {'username': 'toto',
                 'first_name': 'toto',
                 'last_name': 'titi',
                 'email': 'toto@titi.com',
                 'password': 'plouf'}
    user_get = {'username': 'toto',
                'first_name': 'toto',
                'last_name': 'titi',
                'email': 'toto@titi.com',
                'tel': ''}

    def test_add_user(self):
        response = self.client.post('/users/', self.user_post)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), self.user_get)

    def test_get_user(self):
        User.objects.create_user(**self.user_post)
        response = self.client.get('/users/toto/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.user_get)

    def test_update_user_password(self):
        User.objects.create_user(**self.user_post)
        response = self.client.patch('/users/toto/',
                                     data='{"password": "plif"}',
                                     content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.user_get)
        self.assertTrue(User.objects.get(username='toto').check_password('plif'))

    def test_get_all_users(self):
        User.objects.create_user(**self.user_post)
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.user_get])

    def test_search_user(self):
        User.objects.create_user(**self.user_post)
        response = self.client.get('/users/?q=tot')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [self.user_get])

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        super(UserViewTestCase, cls).tearDownClass()
