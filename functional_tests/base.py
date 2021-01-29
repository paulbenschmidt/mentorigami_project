import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time

MAX_WAIT = 10

def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.staging_server = os.environ.get('STAGING_SERVER')
	
    def tearDown(self):  
        self.browser.quit()

    @wait
    def wait_for_page_to_load(self, html_template):
        response = self.browser.get(self.live_server_url)
        self.assertTemplateUsed(response, html_template)
