from pages.auth_page import AuthPage
import time


def test_auth_page_ok(web_browser):
   page = AuthPage(web_browser)
   page.btn_ok_click()
   page.enter_email_ok("yandex@yandex.ru")
   page.enter_pass_ok("qwerty")
   page.btn_ok_sign_in_click()


   time.sleep(5)
   if web_browser.current_url == 'https://connect.ok.ru/':
      web_browser.save_screenshot('result_ok.png')
   else:
       raise Exception("login error")