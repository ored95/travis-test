from django.test import Client
from django.test import TestCase

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_IndexView(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        
    def test_LoginView(self):
        resp = self.client.get('/admin/login/?next=/admin/')
        print(resp)
        self.assertEqual(resp.status_code, 200)

    def test_Login(self):
        resp = self.client.post('/admin/login/?next=/admin/', {'username': 'admin', 'password': '01'})
        self.assertEqual(resp.status_code, 200)