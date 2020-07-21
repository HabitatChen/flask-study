#路由相关文件
# 存放路由注册页面
from application import app

# 通过蓝图来配置页面的路由
# 整体放置在controllers中
from controllers.index import index_page
from controllers.member import member_page

# 引入拦截器
from interceptors.Auth import *
# 根目录路径
app.register_blueprint( index_page, url_prefix='/')

# 登陆注册页面路径
app.register_blueprint( member_page, url_prefix='/member')

from common.libs.UrlManager import UrlManager
# app.add_template_global( UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global( UrlManager.buildUrl, 'buildUrl')