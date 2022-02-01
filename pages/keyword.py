from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from testcases.generic import GENERICLASS
from selenium.webdriver.support.ui import Select


class LOCATERS():
    First_name_Xpath = "//*[@id='vfb-5']"
    Last_name_Xpath = "//*[@id='vfb-7']"
    Gender_Xpath = "//*[@id='vfb-8-1']"
    Address_Xpath = "//*[@id='vfb-13-address']"
    Street_address = "//*[@id='vfb-13-address-2']"
    Optional = "//*[@id='vfb-13-city']"
    city = "//*[@id='vfb-13-zip']"
    State = "//*[@id='vfb-13-country']"
    email = "//*[@id='vfb-14']"
    demo_date = "//*[@id='vfb-18']"
    course = "//*[@id='vfb-20-0']"
    Enter_query = "//*[@id='vfb-23']"
    Verification = "//*[@id='vfb-3']"
    submit = "//*[@id='vfb-4']"
    form_submit = 'elementor-shortcode'
    enter_email_alert = "//*[@id='item-vfb-14']/label[2]"
    empty_fields = "vfb-error"
    alert_of_reuire_fields = "label[generated='true']"

class TESTREGISTRATION(GENERICLASS,LOCATERS):
    def __init__(self):
        self.test_generic = GENERICLASS()


    def enter_the_First_and_last_name(self,Fname,Lname):

        Enter_First_name = self.driver.find_element(By.XPATH,self.First_name_Xpath).send_keys(Fname)
        Enter_last_name =  self.driver.find_element(By.XPATH, self.Last_name_Xpath).send_keys(Lname)

    def select_the_gender(self):
        select_gender = self.driver.find_element(By.XPATH,self.Gender_Xpath).click()
        return select_gender

    def enter_the_address(self,address):
        enter_the_address= self.driver.find_element(By.XPATH,self.Address_Xpath).send_keys(address)
        return enter_the_address

    def enter_the_street_address(self,street_address):
        enter_the_street_address = self.driver.find_element(By.XPATH,self.Street_address).send_keys(street_address)
        return enter_the_street_address

    def enter_the_optional_data(self,optional_data):
        enter_the_data_in_option_field = self.driver.find_element(By.XPATH,self.Optional).send_keys(optional_data)
        return enter_the_data_in_option_field

    def enter_the_city_name(self,city):
        enter_the_city_name = self.driver.find_element(By.XPATH,self.city).send_keys(city)
        return enter_the_city_name

    def select_the_State(self):
        select_state = Select(self.driver.find_element(By.XPATH,self.State))
        select_state.select_by_value("India")

    def enter_the_email(self,email):
        enter_the_email = self.driver.find_element(By.XPATH,self.email).send_keys(email)
        return enter_the_email

    def enter_the_date_of_demo(self,date):
        date_of_demo = self.driver.find_element(By.XPATH,self.demo_date).send_keys(date)
        return date_of_demo

    def select_the_course(self):
        select_the_course = self.driver.find_element(By.XPATH,self.course).click()
        return select_the_course

    def enter_the_query(self,querry):
        enter_query = self.driver.find_element(By.XPATH,self.Enter_query).send_keys(querry)
        return enter_query

    def Enter_verification_digit(self,digit):
        enter_verification = self.driver.find_element(By.XPATH,self.Verification).send_keys(digit)
        return enter_verification

    def click_on_submit_button(self):
        click_on_submit_button = self.driver.find_element(By.XPATH,self.submit).click()
        return click_on_submit_button

    def verify_invalid_email(self):
        alert = self.driver.find_element(By.XPATH, self.enter_email_alert)
        print(alert.text)
        assert alert.text == "Please enter a valid email address."
        print("'Invalid email id entered !!!'")

    def verify_form_is_submitted(self):
        verify = self.driver.find_elements(By.CLASS_NAME,self.form_submit)
        for i in verify:
            try:
                print(i.text)
                assert i.text == "Registration Form is Successfully Submitted. The Transaction ID : NXTGEN1937465"
                print("Able to registered the user sucessfully !!!! Test Case PASS!!!")
                break
            except:
                print("Not able to registered the user")
            finally:
                pass
    def verify_mandatory_fields_empty(self):
       alert_verify= self.driver.find_elements(By.CLASS_NAME,self.empty_fields)
       for alert in alert_verify:
           alert = alert.text
           print(alert)
           if alert == "This field is required.":
                print("PASS-!!!Please fill the all required fields")


    def verify_the_alert_while_enter_the_unexpected_data_in_require_fields(self):
        alert1 = self.driver.find_elements(By.CSS_SELECTOR,self.alert_of_reuire_fields)
        for aler in alert1:
           # print(aler.text)
            if aler.text == "Please enter a valid email address.":
                print("Please enter the valid data in email field")
            elif aler.text == "Please enter only digits.":
                print("Please enter numeric digit only")
            print("PASS!!!!!!!")
