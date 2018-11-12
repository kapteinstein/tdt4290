from django.conf import settings
from ntnui.tests.browser.lib.browser_test_case import ChromeTestCase, FirefoxTestCase
from selenium.webdriver.common.action_chains import ActionChains
from lib.helpers import *

def signing_form_received(browser, server_url, assertEquals, assertTrue):
    login_user(browser, server_url)
    form_creation_page(browser)
    instantiate_form(browser)
    logout(browser)
    login_user(browser, server_url, "leslie@knope.com")
    go_to_signing_form(browser, server_url)
    nexts = browser.find_element_by_xpath("//input[@value = 'Til utfylling']")
    assertEquals(nexts.get_attribute("value"), "Til utfylling")


    



def signing_form_fill_out(browser, server_url, assertEquals, assertTrue):
    
    login_user(browser, server_url)
    form_creation_page(browser)
    instantiate_form(browser)
    logout(browser)
    login_user(browser, server_url, "leslie@knope.com")
    go_to_signing_form(browser, server_url)
    fill_out(browser)
    h3 = browser.find_element_by_xpath("//h3[contains(text(),'Bekreft ditt passord')]")

    assertEquals(h3.text, "Bekreft ditt passord")

def input_password_and_sign(browser):
    password = browser.find_element_by_id("id_password")
    password.send_keys("locoloco")
    browser.find_element_by_xpath("//button[contains(text(),'Signer')]").click()


def sign_form(browser, server_url, assertEquals, assertTrue):
    login_user(browser, server_url)
    form_creation_page(browser)
    instantiate_form(browser)
    logout(browser)
    login_user(browser, server_url, "leslie@knope.com")
    go_to_signing_form(browser, server_url)
    fill_out(browser)
    input_password_and_sign(browser)
    form = browser.find_element_by_xpath("//a[contains(@href, 'signed-form-info')]")

    assertTrue(form)

    



class LoginChrome(ChromeTestCase):
    fixtures = ['database.json']

    def test_signing_form_received(self):
        signing_form_received(self.chrome, self.server_url, self.assertEquals, self.assertTrue)
    
    def test_form_fill_out(self):
        signing_form_fill_out(self.chrome, self.server_url, self.assertEquals, self.assertTrue)

    def test_sign_form(self):
        sign_form(self.chrome, self.server_url, self.assertEquals, self.assertTrue)


class LoginFirefox(FirefoxTestCase):
    fixtures = ['database.json']

    def test_signing_form_received(self):
        signing_form_received(self.firefox, self.server_url, self.assertEquals, self.assertTrue)

    def test_form_fill_out(self):
        signing_form_fill_out(self.firefox, self.server_url, self.assertEquals, self.assertTrue)

    def test_sign_form(self):
        sign_form(self.firefox, self.server_url, self.assertEquals, self.assertTrue)
