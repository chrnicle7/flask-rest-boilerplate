from flask_marshmallow import Marshmallow
from main import app

ma = Marshmallow(app)

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'year', 'author', 'publisher')