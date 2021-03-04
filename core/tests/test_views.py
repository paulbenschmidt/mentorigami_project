from django.test import TestCase
from django.urls import reverse

class CoreTest(TestCase):

    def test_home_uses_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/home.html')

    def test_all_ribbon_buttons_are_available(self):
        response = self.client.get('/')
        self.assertContains(response, 'id="home_icon"')
        self.assertContains(response, 'id="feed_icon"')
        self.assertContains(response, 'id="profile_icon"')
        self.assertContains(response, 'id="settings_icon"')

    def test_all_group_options_are_available(self):
        response = self.client.get('/')
        self.assertContains(response, 'id="groups_container"')
        self.assertContains(response, 'id="mentors_container"')
        self.assertContains(response, 'id="peers_container"')

    # def test_blank_search_entry_does_nothing(self):
