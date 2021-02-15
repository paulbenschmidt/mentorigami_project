from django.test import TestCase
from django.urls import reverse


class SettingsPageTest(TestCase):

    def test_settings_page_uses_settings_template(self):
        response = self.client.get(reverse('settings:settings_page'))
        self.assertTemplateUsed(response, 'settings/settings.html')
