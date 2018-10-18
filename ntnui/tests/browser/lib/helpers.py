from django.conf import settings


def login_user(cls, browser, username="super@admin.com", password="supersuper"):
    browser.get(cls.server_url + '/login/')
    username_input = browser.find_element_by_name('username')
    username_input.send_keys(username)
    password_input = browser.find_element_by_name('password')
    password_input.send_keys(password)
    browser.find_element_by_xpath('//button[text()="Log in"]').click()
    account_p = browser.find_element_by_xpath('//p[text()="Account"]')
