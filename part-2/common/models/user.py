from application import db

class User(db.Model):
    __tablename__ = 'user'

    login_name = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='?????')
    id = db.Column(db.Integer, primary_key=True)
    login_pwd = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    nickname = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
