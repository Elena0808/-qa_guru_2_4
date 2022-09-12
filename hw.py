def print_func_name_and_args(func_name, *args):
    func_name = func_name.__name__.replace('_', ' ').capitalize()
    print(f' Наименование функции: {func_name}')
    for arg_name in args:
        print(f' Значение аргументa: {arg_name}')


def open_browser(browser_name):
    print_func_name_and_args(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_func_name_and_args(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_func_name_and_args(find_registration_button_on_login_page, page_url, button_text)


open_browser('Chrome')
go_to_companyname_homepage('https://yandex.ru/')
find_registration_button_on_login_page('https://yandex.ru/', 'Найти')
