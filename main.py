import data
import helpers

class TestUrbanRoutes:
# Check for server connection
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print ("Connected to the Urban Routes server")
        else:
            print ("Cannot connect to Urban Routes. Check the server is on and still running")
# Setup for test functions
    def test_set_route(self):
        #Add in S8
        print ("function created for set route")
        pass #Placeholder
    def test_select_plan(self):
        #Add in S8
        print ("function created for select plan")
        pass #Placeholder
    def test_fill_phone_number(self):
        #Add in S8
        print ("function created for fill phone number")
        pass #Placeholder
    def test_fill_card(self):
        #Add in S8
        print ("function created for fill card")
        pass #Placeholder
    def test_comment_for_driver(self):
        #Add in S8
        print ("function created for comment for driver")
        pass #Placeholder
    def test_order_blanket_and_handkerchiefs(self):
        #Add in S8
        print ("function created for order blanket and handkerchiefs")
        pass #Placeholder
    def test_order_2_ice_creams(self):
        for ice_cream in range(2): #Loop iterates twice
            #Add in S8
            pass #Placeholder
        #Add in S8
        print ("function created for order 2 ice creams")
        pass #Placeholder
    def test_car_search_model_appears(self):
        #Add in S8
        print ("function created for car search model appears")
        pass #Placeholder



