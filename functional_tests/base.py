import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.staging_server = os.environ.get('STAGING_SERVER')
	
    def tearDown(self):  
        self.browser.quit()
