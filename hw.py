def print_func_name_and_args(func_name, *args):
    func_name = func_name.__name__.replace('_', ' ').capitalize()
    print(f' наименование функции {func_name}')


def open_browser(browser_name):
    print_func_name_and_args(open_browser)


def go_to_companyname_homepage(page_url):
    print_func_name_and_args(go_to_companyname_homepage)


def find_registration_button_on_login_page(page_url, button_text):
    print_func_name_and_args(find_registration_button_on_login_page)


open_browser('Chrome')
go_to_companyname_homepage('https://yandex.ru/')
find_registration_button_on_login_page('https://yandex.ru/', 'Найти')
