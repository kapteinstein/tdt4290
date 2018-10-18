from django.conf import settings
from ntnui.tests.browser.lib.browser_test_case import ChromeTestCase, FirefoxTestCase


def login_general(browser, server_url, assertEquals, assertTrue):
    browser.get(server_url + '/login/')
    username_input = browser.find_element_by_name('username')
    username_input.send_keys("super@admin.com")
    password_input = browser.find_element_by_name('password')
    password_input.send_keys("supersuper")
    browser.find_element_by_xpath('//button').click()
    browser.save_screenshot('screenie.png')
    account_p = browser.find_element_by_xpath("//a[contains(text(),'super@admin.com')]")
    
    assertEquals(account_p.text.lower(), 'super@admin.com')
    assertTrue(
        'href="/a/logout/"' in browser.page_source)


class LoginChrome(ChromeTestCase):
    fixtures = ['database.json']

    def test_login_chrome(self):
        login_general(self.chrome, self.server_url,
                      self.assertEquals, self.assertTrue)


class LoginFirefox(FirefoxTestCase):
    fixtures = ['database.json']

    def test_login_chrome(self):
        login_general(self.firefox, self.server_url,
                      self.assertEquals, self.assertTrue)
