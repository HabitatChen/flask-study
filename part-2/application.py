from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app = Flask( __name__ )

# 设置最大缓存时间为1s
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

app.config['AUTH_COOKIE_NAME'] = 'movie_cat'
app.config['SECRET_KEY'] = '123456imooc'

# 链接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jkla123.0@127.0.0.1/movie_cat'
db = SQLAlchemy( app )

