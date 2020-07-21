from flask import Blueprint, render_template, request, jsonify, make_response, session
from common.libs.UrlManager import UrlManager
from common.models.user import User
from application import db, app


# 可以利用蓝图的前缀 然后将页面层次区分开

# 1. 首先实例化一个member_page
member_page = Blueprint( "member_page", __name__ )

# 2. 使用实例的装饰器
# 即当请求到对应路径时 会自动触发相应方法
@member_page.route('/reg', methods=["GET", "POST"])
def reg():

    if request.method == "GET":
        return render_template('member/reg.html')

    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    # 后端做校验
    if login_name is None or len( login_name ) < 1:
        return jsonify({ "msg": "用户名或密码错误", "status": 0  })

    if login_pwd is None or len( login_pwd ) < 6:
        return jsonify({ "msg": "用户名或密码错误", "status": 0 })

    # 去数据库里面查询是否存在这个用户
    user_info = User.query.filter_by( login_name=login_name ).first()

    # 如果已经存在该用户 则返回 注册失败 如果没有该用户 则想数据库中新增一条用户信息
    if user_info:
        return jsonify({ "msg": "登陆用户名已经注册", "status": 0 })

    # 将数据塞入数据库中
    model_user = User()
    # model_user.id = 1
    model_user.login_name = login_name
    model_user.login_pwd = login_pwd
    # 设置时间
    model_user.created_time = model_user.updated_time = UrlManager.getCurrentTime()

    # 这个几把是干什么用的
    db.session.add(model_user)
    db.session.commit()
    return jsonify({ "msg": "注册成功", "status": 1 })



@member_page.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('member/login.html')

    req = request.values
    print('req %s' % ( req ))

    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    # 后端做校验
    if login_name is None or len(login_name) < 1:
        return jsonify({"msg": "用户名或密码错误", "status": 0})

    if login_pwd is None or len(login_pwd) < 6:
        return jsonify({"msg": "用户名或密码错误", "status": 0})

    # 去数据库里面查询是否存在这个用户
    user_info = User.query.filter_by(login_name=login_name).first()

    if not user_info:
        return jsonify({ "msg": "登陆用户名或密码错误", "status": 0 })

    # 设置cookie
    response = make_response(jsonify({ "msg": "登陆成功", "status": 1 }))
    # response.set_cookie(app.config['AUTH_COOKIE_NAME'], "%s" % (UserService.geneAuthCode(user_info), user_info.id), 60 * 60 * 24)
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], "%s" % ('this is test cookie'), 60 * 60 * 24)
    return response
    # session['uid'] = user_info.id
    # return jsonify({ "msg": "登陆成功", "status": 1 })









