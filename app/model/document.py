from app import db
from app.model.gambar import Gambar

class Bahtsul(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    judul = db.Column(db.String(255), nullable=False)
    tema = db.Column(db.String(255), nullable=False)
    isi = db.Column(db.String(255), nullable=False)
    gambar_id = db.Column(db.BigInteger, db.ForeignKey('gambar.id'), nullable=True)
    
    def __repr__(self):
        return '<Post {}>'.format(self.n)