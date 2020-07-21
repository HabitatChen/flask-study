from application import app
from flask import request, g, redirect
from common.models.user import User

@app.before_request
def before_request():
    user_info = check_login()
    g.current_user = None
    print('------ user_info %s' % (user_info))
    if user_info:
        print('1111')
        g.current_user = user_info
        print('g %s' % (g.current_user))
    return

@app.after_request
def after_request( response ):
    return response

# 用来判断用户是否登陆
def check_login():
    cookies = request.cookies
    cookie_name = app.config['AUTH_COOKIE_NAME']
    auth_cookie = cookies[ cookie_name ] if cookie_name in cookies else None

    if auth_cookie is None:
        return False

    if auth_cookie == 'this is test cookie':
        user_info = User.query.filter_by( login_name='aaa' ).first()
        return user_info