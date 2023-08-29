from pages.registration_page import RegPage
import time

def test_reg_page(web_browser):
   page = RegPage(web_browser)
   page.btn_reg_click()
   page.enter_name("Иван")
   page.enter_second_name("Иванов")
   page.enter_email("yandex@yandex.ru")
   page.enter_pass("Qwerty123")
   page.enter_repeat_pass("Qwerty123")
   page.btn_click()

   if web_browser.current_url == 'https://b2c.passport.rt.ru/account_b2c/page#/':
      web_browser.save_screenshot('reg_page.png')
   else:
      raise Exception("login error")