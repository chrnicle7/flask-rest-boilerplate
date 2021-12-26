from main import db

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    users = db.relationship('User', backref='user', lazy=True)

