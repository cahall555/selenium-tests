import unittest
from selenium import webdriver

class PropertyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to property page
        cls.driver.get('http://www.tigerplazaliving.com')

    # Check to see if search button is enabled
    def test_search_button_test(self):
        search_button = self.driver.find_element_by_class_name("floorplan-search-searchbutton")

        self.assertTrue(search_button.is_enabled())

    #Check to make sure apply now link is displayed
    def test_apply_now_link_displayed(self):
        apply_now_link = self.driver.find_element_by_link_text("APPLY NOW")

        self.assertTrue(apply_now_link.is_displayed())

    @classmethod
    def tearDownClass(cls):
        #close browser
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
