from urllib.parse import urlparse
import webbrowser

from hm_auth import do_auth
from lluser.store_userinfo import *
from hm_auth.config.url import *


def do_ping(ip):
    os.system('start ping '+ip)


def open_on_browser(url):
    webbrowser.open(url)


if __name__ == '__main__':
    print('(*｀∀´*)ノ亻!, 欢迎使用auth~ ')

    dump_user_mutual()
    print()

    print('\n正在发送认证请求...\n')
    try:
        if do_auth.do_auth(*load_user()):
            print("Portal认证成功")
        else:
            print('Portal认证失败，请检查账户信息')
    except TimeoutError or ConnectionError as e:
        print(e)
        y_or_n = input('\n是否使用? [ping %s] (y/n)' % urlparse(auth_get_url).netloc)
        if y_or_n in ('y', 'Y'):
            do_ping(urlparse(auth_get_url).netloc)

        y_or_n = input('\n是否打开浏览器访问认证页面? [%s] (y/n)' % auth_page_get_url)
        if y_or_n in ('y', 'Y'):
            open_on_browser(auth_page_get_url)

    except Exception as e:
        print(e)

    finally:
        input('\nenter any key...')

