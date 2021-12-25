from main import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(50))
    password = db.Column(db.String(200))
    address = db.Column(db.String(500))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    def __init__(self, id, name, email, password, address, role_id):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.role_id = role_id

    def __getitem__(self, arg):
        return arg

    def __setitem__(self, arg):
        return arg

    def json(self):
        return {"id": self.id, "name": self.name, "address": self.address, "role_id": self.role_id}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get_or_404(id)

    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def find_by_role(cls, role_id):
        return cls.query.filter_by(role_id=role_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()