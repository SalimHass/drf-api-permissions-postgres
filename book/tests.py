from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TestBookView(TestCase):

    def setUp(self):
        self.client.login(username="testinguser", password="dlasldhas")
    
    def test_authetication_required(self):
        self.client.logout()
        url = reverse('books_list')
        # 403 Forbidden
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)