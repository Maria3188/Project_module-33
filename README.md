Тест test_auth_page_email:

Позитивный тест проверки авторизации на сайте Ростелеком, для успешной авторизации пользователю необходимо иметь эл. почту и пароль

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_auth_page.py

Тест test_auth_page_phone:

Позитивный тест проверки авторизации на сайте Ростелеком, для успешной авторизации пользователю необходимо иметь номер телефона и пароль

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_auth_page_phone.py

Тест test_auth_page_login:

Позитивный тест проверки авторизации на сайте Ростелеком, для успешной авторизации пользователю необходимо иметь логин и пароль

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_auth_page_login.py

Тест test_auth_page_account:

Негативный тест проверки авторизации на сайте Ростелеком, для авторизации пользователю необходимо иметь номер лицевого счета и пароль

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_auth_page_account.py

Тест test_auth_page_vk:

Позитивный тест проверки авторизации пользователя на сайте Ростелеком по его аккаунту в социальной сети VK, для успешной авторизации пользователю необходимо иметь действующий аккаунт в VK

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_auth_page_vk.py

Тест test_auth_page_ok:

Позитивный тест проверки авторизации пользователя на сайте Ростелеком по его аккаунту в социальной сети Одноклассники, для успешной авторизации пользователю необходимо иметь действующий аккаунт в Одноклассниниках

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_auth_page_ok.py

Тест test_auth_page_mail:

Позитивный тест проверки авторизации пользователя на сайте Ростелеком по его аккаунту в Mail, для успешной авторизации пользователю необходимо иметь действующий аккаунт в Mail

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_auth_page_mail.py

Тест test_auth_page_yandex:

Позитивный тест проверки авторизации пользователя на сайте Ростелеком по его аккаунту в Яндексе, для успешной авторизации пользователю необходимо иметь действующий аккаунт в Яндексе

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_auth_page_yandex.py

Тест test_reg_page:

Позитивный тест проверки регистрации пользователя на сайте Ростелеком, для успешной авторизации пользователю необходимо ввести Имя, Фамилию, ввести эл. почту и пароль

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_reg_page.py

Тест test_reg_page_latiniza:

Негативный тест проверки регистрации пользователя на сайте Ростелеком, для успешной авторизации пользователю необходимо ввести Имя, Фамилию латинскими буквами.

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_reg_latiniza.py

Тест test_reg_page_invalid_pass:

Негативный тест проверки регистрации пользователя на сайте Ростелеком, для авторизации пользователю необходимо ввести Имя, Фамилию эл. почту и пароль(менее 8 символов).

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_reg_invalid_pass.py

Тест test_reg_page_empty_pass:

Негативный тест проверки регистрации пользователя на сайте Ростелеком, для авторизации пользователю необходимо ввести Имя, Фамилию, эл. почту, пароль и поле “Подтверждение пароля” оставить пустым .

Команда для запуска теста:

python -m pytest -v --driver Firefox --driver-path /Users/maria/Desktop/test/geckodriver.exe test_reg_empty_pass.py
