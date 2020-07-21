from flask import Blueprint, render_template, g
from common.models.user import User

# 可以利用蓝图的前缀 然后将页面层次区分开

# 1. 首先实例化一个index_page
index_page = Blueprint( "index_page", __name__ )

# 2. 使用实例的装饰器
# 即当请求到对应路径时 会自动触发相应方法
@index_page.route('/')
def index():
    context = {
        "name": "index page"
    }
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template("index.html", **context)

@index_page.route('/sql-test')
def sql_test():
    context = {
        "name": 'habtatchen'
    }
    # from sqlalchemy import text
    # from application import app, db
    # sql = text( 'select * from `user`' )
    # print(' ==== = = == = ')
    # result = db.engine.execute( sql )
    # app.logger.info( '-------' )
    # app.logger.info( result )

    # 引入User 然后使用新的sql查询方式
    result = User.query.all()
    context['result'] = result

    if 'current_user' in g:
        context['current_user'] = g.current_user

    return render_template("index.html", **context)

