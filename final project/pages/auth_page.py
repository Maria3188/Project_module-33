from .base_page import BasePage
from .locators import AuthLocators

import  time,os

class AuthPage(BasePage):

   def __init__(self, driver,timeout=10):
       super().__init__(driver, timeout)
       url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
       driver.get(url)


   def enter_email(self, value):
       self.driver.find_element(*AuthLocators.AUTH_EMAIL).send_keys(value)

   def enter_pass(self, value):
       self.driver.find_element(*AuthLocators.AUTH_PASS).send_keys(value)

   def enter_phone(self, value):
       self.driver.find_element(*AuthLocators.AUTH_PHONE).send_keys(value)

   def enter_login(self, value):
       self.driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(value)

   def enter_account(self, value):
       self.driver.find_element(*AuthLocators.AUTH_ACCOUNT).send_keys(value)

   def enter_email_for_vk(self, value):
       self.driver.find_element(*AuthLocators.AUTH_VK_EMAIL).send_keys(value)
       time.sleep(3)  # ждем реакции

   def enter_email_ok(self, value):
       self.driver.find_element(*AuthLocators.AUTH_EMAIL_OK).send_keys(value)
       time.sleep(3)  # ждем реакции

   def enter_pass_ok(self, value):
       self.driver.find_element(*AuthLocators.AUTH_PASSWORD_OK).send_keys(value)
       time.sleep(3)  # ждем реакции

   def btn_ok_sign_in_click(self):
       self.driver.find_element(*AuthLocators.AUTH_OK_SIGN_IN).click()
       time.sleep(3) #ждем реакции

   def btn_click(self):
       self.driver.find_element(*AuthLocators.AUTH_BTN).click()
       time.sleep(3) #ждем реакции

   def btn_acc_click(self):
       self.driver.find_element(*AuthLocators.AUTH_BTN_ACC).click()
       time.sleep(3) #ждем реакции

   def btn_vk_click(self):
       self.driver.find_element(*AuthLocators.AUTH_BTN_VK).click()
       time.sleep(3) #ждем реакции

   def btn_vk_sign_in_click(self):
       self.driver.find_element(*AuthLocators.AUTH_VK_SIGN_IN).click()
       time.sleep(3) #ждем реакции

   def btn_ok_click(self):
       self.driver.find_element(*AuthLocators.AUTH_BTN_OK).click()
       time.sleep(3) #ждем реакции

   def btn_mail_click(self):
       self.driver.find_element(*AuthLocators.AUTH_BTN_MAIL).click()
       time.sleep(3) #ждем реакции

   def btn_yandex_click(self):
       self.driver.find_element(*AuthLocators.AUTH_BTN_YANDEX).click()
       time.sleep(3) #ждем реакции

   def btn_email_click(self):
       self.driver.find_element(*AuthLocators.AUTH_BTN_EMAIL).click()
       time.sleep(3) #ждем реакции


   def btn_login_click(self):
       self.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
       time.sleep(3) #ждем реакции

   def enter_email_for_mail(self, value):
       self.driver.find_element(*AuthLocators.AUTH_EMAIL_MAIL).send_keys(value)
       time.sleep(3)  # ждем реакции

   def enter_pass_for_mail(self, value):
       self.driver.find_element(*AuthLocators.AUTH_PASSWORD_MAIL).send_keys(value)
       time.sleep(3)  # ждем реакции

   def btn_mail_sign_in_click(self):
       self.driver.find_element(*AuthLocators.AUTH_MAIL_SIGN_IN).click()
       time.sleep(3) #ждем реакции

   def enter_email_for_yandex(self, value):
       self.driver.find_element(*AuthLocators.AUTH_EMAIL_YANDEX).send_keys(value)
       time.sleep(3)  # ждем реакции

   def btn_yandex_sign_in_click(self):
       self.driver.find_element(*AuthLocators.AUTH_YANDEX_SIGN_IN).click()
       time.sleep(3) #ждем реакции

