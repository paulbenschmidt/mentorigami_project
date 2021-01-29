from django.test import TestCase

class HomePageTest(TestCase):

    def test_home_uses_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

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

    def test_search_ribbon_goes_to_search_page(self):
        search_item = "Underwater basket weaving"
        response = self.client.get('/search/', data={'text': search_item})
        search_item_formatted = search_item.replace(' ', '_').lower()
        print(response)
        self.assertRedirects(response, f'/search/{search_item_formatted}/')



    # def test_blank_search_entry_does_nothing(self):
