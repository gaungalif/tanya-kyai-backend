from app.model.post import Post
from app.model.tanya import Tanya 

from app import response, app, db
from flask import request

def TanyaList():
    try:
        tanya = Tanya.query.all()
        data = transform(tanya)
        return response.success(data, "Data berhasil didapatkan")
    except Exception as e:
        print(e)
        
def singleTransform(tanya):
    data = {
        'id' : tanya.id,
        'tema' : tanya.tema,
        'judul' : tanya.judul,
        'isi' : tanya.isi,
        'gambar_id' : tanya.gambar_id
    }
    return data

def transform(tanya):
    array = []
    for i in tanya:
        array.append(singleTransform(i))
    return array

def TanyabyID(id):
    try:
        tanya = Tanya.query.filter_by(id=id).first()
        data = singleTransform(tanya)
        return response.success(data, "Data berhasil didapatkan")
    
    except Exception as e:
        print(e)