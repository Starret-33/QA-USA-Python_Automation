import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    # Addresses
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Tariff and call button
    supportive_plan_card = (By.XPATH, '//div[contains(text(), "Supportive")]')
    get_current_selected_plan = (By.XPATH, '//div[contains(text(), "Supportive")]//..')
    active_plan_card = (By.XPATH, '//div[@class = "card active"]//div[@class = "card-title"]')
    call_taxi_button = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    # Filling in the phone number
    phone_number_input = (By.XPATH, '//div[@class= "np-button"]//div[contains(text(), "phone number")]')
    phone_number_label = (By.ID, "phone")
    phone_number_next_button = (By.CSS_SELECTOR, "button.full")
    phone_number_code_label = (By.ID, "code")
    get_enter_code_sms_text = (By.XPATH, '//div[text()= "Enter the code from the SMS"]')
    confirm_button = (By.XPATH, '//div[text()= "Confirm"]')
    phone_number = (By.CLASS_NAME, "np-text")
    # Adding a credit card
    payment_method = (By.XPATH, '//div[@class= "pp-button filled"]//div[contains(text(), "Payment method")]')
    add_card = (By.XPATH, '//div[contains(text(), "Adding a card")]')
    card_number_input = (By.ID, "number")
    card_code_input = (By.XPATH, '(//input[@class= "card-input"])[2]')
    link_button = (By.XPATH, '//button[contains(text(), "Link")]')
    validate_card_input = (By.XPATH, '//div[@class= "pp-checkbox"]')
    current_payment_method = (By.CLASS_NAME, "pp-value-text")
    close_payment_screen = (By.XPATH, '//button[contains(@class= "close-button") and contains(@class= "section-close")]')
    # Writing a comment for the driver
    driver_comment = (By.XPATH, '//input[@name="comment" and @type="text"]')
    # Ordering a blanket and handkerchiefs
    click_blanket_and_handkerchiefs = (By.XPATH, '//span[@class= "slider round"][1]')
    validate_click_blanket_and_handkerchiefs = (By.XPATH, '//input[@type= "checkbox"][2]')
    # Ordering 2 ice cream
    add_ice_cream = (By.XPATH, '//div[contains(@class, "counter-plus")]')
    # Car search window
    select_supportive_tariff = (By.XPATH, '//div[contains(text(), "Supportive")]')
    order_button = (By.XPATH, '//button[contains(text(), "Order")]')
    car_search_modal = (By.XPATH, '//div[contains(@class, "car-search-modal")]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        from_field = self.driver.find_element(*self.from_field)
        from_field.send_keys(from_address)
        time.sleep(1)

    def set_to(self, to_address):
        to_field = self.driver.find_element(*self.to_field)
        to_field.send_keys(to_address)
        time.sleep(1)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get.property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get.property('value')

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(self.call_taxi_button))
        self.driver.find_element(*self.call_taxi_button).click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        time.sleep(2)
        self.click_call_taxi_button()

    def enter_phone_number(self, phone_number):
       self.driver.find_element(*self.phone_number_input).click()
       time.sleep(2)
       self.driver.find_element(*self.phone_number_label).click()
       time.sleep(1)
       self.driver.find_element(*self.phone_number_next_button).click()
       time.sleep(2)
       code = retrieve_phone_code(self.driver)
       self.driver.find_element(*self.phone_number_code_label).send_keys(code)
       time.sleep(1)
       self.driver.find_element(*self.confirm_button).click()
       time.sleep(2)

    def get_phone(self):
        return self.driver.find_element(*self.phone_number).text

    def enter_payment_method(self, card_number, card_code):
        self.driver.find_element(*self.payment_method).click()
        time.sleep(1)
        self.driver.find_element(*self.add_card).click()
        time.sleep(1)
        self.driver.find_element(*self.card_number_input).send_keys(card_number)
        time.sleep(2)
        self.driver.find_element(*self.card_code_input).send_keys(card_code)
        time.sleep(2)
        self.driver.find_element(*self.link_button).click()
        time.sleep(1)
        self.driver.find_element(*self.validate_card_input).click()
        time.sleep(2)


    def click_close_payment_screen(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(self.close_payment_screen))
        self.driver.find_element(*self.close_payment_screen).click()

    def get_current_payment_method(self):
        return self.driver.find_element(*self.current_payment_method).text

    def driver_comment_value(self, message):
        self.driver.find_element(*self.driver_comment).send_keys(message)
        time.sleep(2)

    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.click_blanket_and_handkerchiefs).click()
        time.sleep(2)

    def get_order_requirements_checked(self):
        return self.driver.find_element(*self.click_blanket_and_handkerchiefs).get.property('checked')

    def click_add_ice_cream(self):
        for _ in range(2):  # Loop iterates twice
            self.driver.find_element(*self.add_ice_cream).click()
            time.sleep(2)

    def search_supportive_tariff(self):
        self.driver.find_element(*self.select_supportive_tariff).click()
        time.sleep(2)

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()
        time.sleep(2)

    def is_car_search_modal_visible(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.car_search_modal))
        return self.driver.find_element(*self.car_search_modal).is_displayed()






