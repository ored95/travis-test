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
        self.assertEqual(resp.status_code, 200)

    def test_Login(self):
        resp = self.client.post('/admin/login/?next=/admin/', {'username': 'admin', 'password': '01'})
        self.assertEqual(resp.status_code, 200)

class TestREST(TestCase):
    def setUp(self):
        self.client = Client()

    # incorrect tests
    def test_01(self):
        resp = self.client.post('/', {'x-value': 'a', 'y-value': 4.5, 'z-value': 5.111})
        self.assertEqual(resp.status_code, 404);

    def test_02(self):
        resp = self.client.post('/', {'x-value': '0', 'y-value': '1e', 'z-value': 2})
        self.assertEqual(resp.status_code, 404);

    def test_03(self):
        resp = self.client.post('/', {'x-value': -12, 'y-value': "just for fun", 'z-value': 'ok'})
        self.assertEqual(resp.status_code, 404);
    
    # correct test
    def test_11(self):
        resp = self.client.post('/', {'x-value': 3, 'y-value': 4, 'z-value': 5})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['triplet'], "(3, 4, 5)")
        self.assertEqual(resp.context['result'], "A Pythagore's triplet")

    def test_12(self):
        resp = self.client.post('/', {'x-value': 1, 'y-value': 1, 'z-value': 0})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['triplet'], "(1, 1, 0)")
        self.assertEqual(resp.context['result'], "A Pythagore's triplet")

    def test_13(self):
        resp = self.client.post('/', {'x-value': -12, 'y-value': -13, 'z-value': 5})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['triplet'], "(-12, -13, 5)")
        self.assertEqual(resp.context['result'], "A Pythagore's triplet")

    def test_14(self):
        resp = self.client.post('/', {'x-value': 2.0, 'y-value': 3.0, 'z-value': 4.0})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['triplet'], "(2.0, 3.0, 4.0)")
        self.assertEqual(resp.context['result'], "A non-Pythagore's triplet")

    def test_15(self):
        resp = self.client.post('/', {'x-value': 13, 'y-value': 5.01, 'z-value': 12})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['triplet'], "(13, 5.01, 12)")
        self.assertEqual(resp.context['result'], "A non-Pythagore's triplet")

    def test_16(self):
        resp = self.client.post('/', {'x-value': .1, 'y-value': .1, 'z-value': .0001})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['triplet'], "(0.1, 0.1, 0.0001)")
        self.assertEqual(resp.context['result'], "A non-Pythagore's triplet")