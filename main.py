from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage

class TestUrbanRoutes:
# Check for server connection
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print ("Connected to the Urban Routes server")
        else:
            print ("Cannot connect to Urban Routes. Check the server is on and still running")

# Setup for test functions
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.supportive_plan_card()
        if routes_page.get_current_selected_plan() != 'Supportive':
            routes_page.supportive_plan_card()
        assert routes_page.get_current_selected_plan() == 'Supportive'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(data.PHONE_NUMBER)
        routes_page.get_enter_code_sms_text(code)

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.enter_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.get_current_payment_method() == 'Card'

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.enter_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.driver_comment(data.MESSAGE_FOR_DRIVER)
        comment_value = routes_page.driver_comment_value()
        assert comment_value() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.enter_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.driver_comment(data.MESSAGE_FOR_DRIVER)
        routes_page.order_blanket_and_handkerchiefs()
        assert routes_page.validate_click_blanket_and_handkerchiefs()

    def test_order_2_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.enter_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.driver_comment(data.MESSAGE_FOR_DRIVER)
        routes_page.click_add_ice_cream()

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.enter_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.driver_comment(data.MESSAGE_FOR_DRIVER)
        routes_page.select_supportive_tariff()
        routes_page.click_order_button()
        assert routes_page.is_car_search_modal_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



