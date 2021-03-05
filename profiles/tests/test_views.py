from django.test import TestCase
from django.urls import reverse


class ProfilesPageTest(TestCase):

    def test_settings_page_uses_settings_template(self):
        response = self.client.get(reverse('profiles:settings_page'))
        self.assertTemplateUsed(response, 'profiles/settings.html')
