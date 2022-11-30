from app import db
from app.model.tanya import Tanya
from app.model.gambar import Gambar

class Post(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    isi = db.Column(db.String(1500), nullable=False)
    tanya_id = db.Column(db.BigInteger, db.ForeignKey('tanya.id'), nullable=True)
    # gambar_id = db.Column(db.BigInteger, db.ForeignKey('gambar.id'), nullable=True)
    
    def __repr__(self):
        return '<Post {}>'.format(self.name)