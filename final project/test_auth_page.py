from pages.auth_page import AuthPage


def test_auth_page_email(web_browser):
   page = AuthPage(web_browser)
   page.btn_email_click()
   page.enter_email("yandex@yandex.ru")
   page.enter_pass("qwerty")
   page.btn_click()


   if web_browser.current_url == 'https://b2c.passport.rt.ru/account_b2c/page#/':
      web_browser.save_screenshot('result_email.png')
   else:
      raise Exception("login error")

