from .base_page import BasePage
from .registration_locators import RegLocators

import  time,os

class RegPage(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
       driver.get(url)

   def btn_reg_click(self):
       self.driver.find_element(*RegLocators.REG).click()
       time.sleep(3)  # ждем реакции

   def enter_name(self, value):
       self.driver.find_element(*RegLocators.REG_NAME).send_keys(value)
       time.sleep(3)  # ждем реакции

   def enter_second_name(self, value):
       self.driver.find_element(*RegLocators.REG_SECOND_NAME).send_keys(value)
       time.sleep(3)  # ждем реакции

   def enter_email(self, value):
       self.driver.find_element(*RegLocators.REG_EMAIL).send_keys(value)
       time.sleep(3)  # ждем реакции

   def enter_pass(self, value):
       self.driver.find_element(*RegLocators.REG_PASSWORD).send_keys(value)
       time.sleep(3)  # ждем реакции

   def enter_repeat_pass(self, value):
       self.driver.find_element(*RegLocators.REG_REPEAT_PASSWORD).send_keys(value)
       time.sleep(3)  # ждем реакции

   def btn_click(self):
       self.driver.find_element(*RegLocators.REG_BTN).click()
       time.sleep(3) #ждем реакции

