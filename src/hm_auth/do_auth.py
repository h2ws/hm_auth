import requests
from urllib.parse import urlparse

from requests.exceptions import ReadTimeout

from hm_auth.config.url import *
from hm_auth.config.header import *

tip = '您可能不在局域网内\n'
tip += '建议使用ping命令检查与 %s 的连通性' % urlparse(auth_get_url).netloc


def raise_timeout():
    msg = '认证URL (%s) 响应超时' % auth_get_url
    msg += '\n'
    msg += tip
    raise TimeoutError(msg)


def raise_data_invalid(resp):
    msg = '响应数据异常\n'
    msg += '响应正文: \n'
    msg += str(resp.content) + '\n'
    msg += tip
    raise ConnectionError(msg)


def do_auth(username, password):
    conn = requests.session()
    auth_params = {'userName': username, 'userPasswd': password, 'userCommand': 'userAuth'}

    try:
        resp = conn.get(
            auth_get_url,
            params=auth_params,
            headers=auth_headers,
            allow_redirects=False,
            timeout=5
        )

        if not resp.headers.__contains__('Location'):
            raise_data_invalid(resp)

        return resp.headers['Location'] == auth_message_get_url

    except ReadTimeout:
        raise_timeout()

    finally:
        conn.close()


