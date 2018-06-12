from selenium import webdriver
from time import gmtime, strftime
import unittest


class ApplyNow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to home page
        self.driver.get("http://liveskybox.com/")

    def test_apply_now(self):
        driver = self.driver

        # navigate to apply form
        driver.find_element_by_css_selector("span.headerText.hidden-xs").click()
        driver.find_element_by_css_selector("li.floor-plans > a").click()
        driver.find_element_by_xpath("//div[starts-with(@id,'unit_show_hide')]").click()
        #driver.switch_to_active_element()
        #pop_up_id = driver.current_window_handle
        driver.find_element_by_partial_link_text("Next").click()
        driver.find_element_by_xpath("//button[@type='button'][2]").click()
        driver.find_element_by_xpath("//span[@type='button'][2]").click()

        # sign in link in upper right hand corner
        sign_in_link = \
            driver.find_element_by_link_text("SIGN IN")

        # check sign in link is displayed # and enabled
        self.assertTrue(sign_in_link.is_displayed() and sign_in_link.is_enabled())

        # check title
        self.assertEquals("Register", driver.title)

        # get all the fields from apply now form
        first_name = driver.find_element_by_id("firstName")
        last_name = driver.find_element_by_id("lastName")
        phone_number = driver.find_element_by_id("phone")
        email_address = driver.find_element_by_id("email")
        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")
        confirm_password = driver.find_element_by_id("confirmPassword")
        select_traffic_source = driver.find_element_by_id("trafficSource")
        select_leasing_agent = driver.find_element_by_id("agent")
        agree = driver.find_element_by_class_name("custom-checkmark")
        #submit_button = driver.\
         #   find_element_by_xpath("//button[@title='Register']")

        # check maxlength of first name and # last name textbox
        self.assertEqual("30", first_name.get_attribute("maxlength"))
        self.assertEqual("30", last_name.get_attribute("maxlength"))

        # check all fields are enabled
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and email_address.is_enabled() and phone_number.is_enabled() and agree.is_enabled() and password.is_enabled() and confirm_password.is_enabled() and select_traffic_source.is_enabled() and select_leasing_agent.is_enabled())

        # check agree to terms and conditions is not checked
        self.assertFalse(agree.is_selected())

        # check default selection is -Please select-
        self.assertEqual("-Please select-",select_traffic_source.first_selected_option.text)

        #check number of options in dropdown
        self.assertEqual(2,len(select_traffic_source.options))

        username = "user_" + strftime("%Y%m%d%H%M%S", gmtime())
        # fill out all the fields
        first_name.send_keys("Test")
        last_name.send_keys(user_name)
        agree.click()
        email_address.send_keys(user_name + "@example.com")
        password.send_keys("tester")
        confirm_password.send_keys("tester")
        select_traffic_source.select_by_visable_text("Banner")
        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
