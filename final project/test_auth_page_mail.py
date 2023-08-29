from pages.auth_page import AuthPage
import time


def test_auth_page_mail(web_browser):
   page = AuthPage(web_browser)
   page.btn_mail_click()
   page.enter_email_for_mail("syandex@yandex.ru")
   page.enter_pass_for_mail("qwerty123")
   page.btn_mail_sign_in_click()

   time.sleep(5)
   if web_browser.current_url == 'https://connect.mail.ru/oauth//mail/':
      web_browser.save_screenshot('result_vk.png')
   else:
      raise Exception("login error")