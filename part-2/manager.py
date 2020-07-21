# 从全局变量中 拿到app
from application import app
from www import *
app.run(host='127.0.0.1', port=3000, debug=True)
