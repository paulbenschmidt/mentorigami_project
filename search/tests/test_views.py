from django.test import TestCase
from django.urls import reverse


class SearchPageTest(TestCase):

    def test_search_uses_template(self):
        response = self.client.get(reverse('search:search_results'))
        self.assertTemplateUsed(response, 'search_results.html')

    def test_search_url_returns_200(self):
        data = {'search': 'Underwater basket weaving'} # can add more params here
        response = self.client.get(reverse('search:search_results'), data=data)
        self.assertEqual(response.status_code, 200)
