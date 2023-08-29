from pages.auth_page import AuthPage
import time


def test_auth_page_vk(web_browser):
   page = AuthPage(web_browser)
   page.btn_vk_click()
   page.enter_email_for_vk("sc3110@yandex.ru")
   page.btn_vk_sign_in_click()

   time.sleep(5)
   if web_browser.current_url == 'https://id.vk.com/auth/':
      web_browser.save_screenshot('result_vk.png')
   else:
      raise Exception("login error")