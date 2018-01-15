from django.urls import resolve
from django.test import TestCase
from awsm.views import index_page

# Create your tests here.
class IndexPageTest(TestCase):

    def test_for_index_page(self):
        found = resolve('/awsm/')
        self.assertEqual(found.func, index_page)
