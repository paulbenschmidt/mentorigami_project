from django.test import TestCase
from django.urls import reverse


class SearchPageTest(TestCase):

    def test_search_uses_template(self):
        response = self.client.get(reverse('search:search'))
        self.assertTemplateUsed(response, 'search.html')
