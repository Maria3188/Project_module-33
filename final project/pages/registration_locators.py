from selenium.webdriver.common.by import By

class RegLocators:
   REG = (By.ID, "kc-register")
   REG_NAME = (By.NAME, "firstName")
   REG_SECOND_NAME = (By.NAME, "lastName")
   REG_EMAIL = (By.ID, "address")
   REG_PASSWORD = (By.ID, "password")
   REG_REPEAT_PASSWORD = (By.ID, "password-confirm")
   REG_BTN = (By.CLASS_NAME, "rt-btn")
