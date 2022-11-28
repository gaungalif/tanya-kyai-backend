from app import db
import json
from app.model.post import Post
from app.model.gambar import Gambar

class Tanya(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    googleuid = db.Column(db.String(100), nullable=False)
    tema = db.Column(db.String(50), nullable=False)
    judul = db.Column(db.String(50), nullable=False)
    isi = db.Column(db.String(255), nullable=False)
    gambar_id = db.Column(db.BigInteger, db.ForeignKey('gambar.id'), nullable=True)
    
    def __repr__(self):
        return '<pertanyaan {}>'.format(self.name)