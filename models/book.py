from main import db

class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    year = db.Column(db.Integer)
    author = db.Column(db.String(200))
    publisher = db.Column(db.String(200))

    def __init__(self, title, year, author, publisher):
        self.title = title
        self.year = year
        self.author = author
        self.publisher = publisher
    
    def __getitem__(self, arg):
        return arg

    def __setitem__(self, arg):
        return arg

    def json(self):
        return {"title": self.title, "year": self.year, "author": self.author, "publisher": self.publisher}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get_or_404(id)

    def find_by_name(cls, name):
        search = "%{}%".format(name)
        return cls.query.filter_by(name=BookModel.name.like(search)).all()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
