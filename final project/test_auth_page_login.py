from pages.auth_page import AuthPage
import time


def test_auth_page_login(web_browser):
   page = AuthPage(web_browser)
   page.btn_login_click()
   page.enter_login("MariaM")
   page.enter_pass("qwerty123")
   page.btn_click()

   time.sleep(5)

   if web_browser.current_url == 'https://b2c.passport.rt.ru/account_b2c/page#/':
      web_browser.save_screenshot('result_vk.png')
   else:
      raise Exception("login error")

