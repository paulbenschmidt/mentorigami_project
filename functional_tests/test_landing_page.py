from selenium.webdriver.common.keys import Keys

from base import FunctionalTest

class LandingPageTest(FunctionalTest):
    def test_user_can_search_channels_from_landing_page(self):
        # Paula hears about a new mentor site for learning and goes to check it out
        self.browser.get(self.live_server_url)

        # On the main landing page, she sees a ribbon on the top with a "search" feature
        search_ribbon = self.browser.find_element_by_id('search_ribbon')
        
        # Paula clicks on it and searches for her new hobby: underwater basket weaving
        search_ribbon.send_keys('Underwater basket weaving')
        search_ribbon.send_keys(Keys.ENTER)

        # She is taken to a separate page and sees information on all the mentors, groups, and peers
        self.assertRedirects(self, 'search_page.html')
        # self.fail("The search did not go to the search page")
