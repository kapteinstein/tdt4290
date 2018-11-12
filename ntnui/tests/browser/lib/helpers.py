from django.conf import settings


def form_creation_page(browser):
    schema_navbar_element = browser.find_element_by_xpath("//a[contains(text(),'skjema')]").click()
    schema_create_tab_element = browser.find_element_by_xpath("//a[contains(@href, 'instantiator')]").click()

def login_user(browser, server_url, username="ron@swanson.com", password="locoloco"):
    browser.get(server_url + '/login/')
    username_input = browser.find_element_by_name('username')
    username_input.send_keys(username)
    password_input = browser.find_element_by_name('password')
    password_input.send_keys(password)
    browser.find_element_by_xpath('//button').click()

def instantiate_form(browser):
    select_leslie = browser.find_element_by_xpath("//option[contains(text(),'Leslie Knope')]").click()
    send = browser.find_element_by_xpath("//input[contains(@value, 'Send')]").click()

def logout(browser):
    lo = browser.find_element_by_xpath("//a[contains(@href, 'logout')]")
    browser.execute_script("arguments[0].click()", lo)

def go_to_signing_form(browser, server_url):
    browser.save_screenshot('screenie.png')
    schema_navbar_element = browser.find_element_by_xpath("//a[contains(text(),'skjema')]").click()
    schema_create_tab_element = browser.find_element_by_xpath("//a[contains(@href, 'incoming-list')]").click()
    go_to_schema = browser.find_element_by_xpath("//a[contains(text(),'ansettelse')]").click()

def fill_out(browser):
    nexts = browser.find_element_by_xpath("//input[@value = 'Neste']").click()
    
    position = browser.find_element_by_xpath("//option[contains(text(),'Trener')]")
    position.click()
    compensation = browser.find_element_by_xpath("//option[contains(text(),'treningskort')]")
    compensation.click()
    date = browser.find_element_by_xpath("//input[contains(@type, 'date')]")
    browser.save_screenshot('screenie2.png')
    browser.execute_script("arguments[0].type='text';", date)
    date.clear()
    date.send_keys("01/01/2020")
    nexts = browser.find_element_by_xpath("//input[@value = 'Neste']").click()