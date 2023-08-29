from pages.auth_page import AuthPage
import time


def test_auth_page_yandex(web_browser):
   page = AuthPage(web_browser)
   page.btn_yandex_click()
   page.enter_email_for_yandex("89834254925")
   page.btn_yandex_sign_in_click()

   time.sleep(5)
   if web_browser.current_url == 'https://passport.yandex.ru/auth/':
      web_browser.save_screenshot('result_ya.png')
   else:
      raise Exception("login error")