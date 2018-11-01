from django.conf import settings
from ntnui.tests.browser.lib.browser_test_case import ChromeTestCase, FirefoxTestCase
from lib.helpers import *


def login_general(browser, server_url, assertEquals, assertTrue):
    login_user(browser, server_url)
    account_p = browser.find_element_by_xpath("//a[contains(text(),'ron@swanson.com')]")
    
    assertEquals(account_p.text.lower(), 'ron@swanson.com')
    assertTrue(
        'href="/a/logout/"' in browser.page_source)

    

def go_to_form_creation_page(browser, server_url, assertEquals, assertTrue):
    login_user(browser, server_url)
    form_creation_page(browser)
    span = browser.find_element_by_xpath("//span[contains(text(),'Send skjema')]")
    assertEquals(span.text, 'Send skjema')

def create_schema(browser, server_url, assertEquals, assertTrue):
    login_user(browser, server_url)
    form_creation_page(browser)
    instantiate_form(browser)

    h2 = browser.find_element_by_xpath("//h2[contains(text(),'Utsendte skjema')]")

    assertEquals(h2.text, 'Utsendte skjema')






class LoginChrome(ChromeTestCase):
    fixtures = ['database.json']

    def test_login_chrome(self):
        login_general(self.chrome, self.server_url,
                      self.assertEquals, self.assertTrue)
        
    def test_goto_schema(self):
        go_to_form_creation_page(self.chrome, self.server_url, self.assertEquals, self.assertTrue)
    
    def test_create_schema(self):
        create_schema(self.chrome, self.server_url, self.assertEquals, self.assertTrue)
        


class LoginFirefox(FirefoxTestCase):
    fixtures = ['database.json']

    def test_login_chrome(self):
        login_general(self.firefox, self.server_url,
                      self.assertEquals, self.assertTrue)

    def test_goto_schema(self):
        go_to_form_creation_page(self.firefox, self.server_url, self.assertEquals, self.assertTrue)

    def test_create_schema(self):
        create_schema(self.firefox, self.server_url, self.assertEquals, self.assertTrue)
