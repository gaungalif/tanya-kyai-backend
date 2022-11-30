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

    # id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    # googleuid = db.Column(db.String(100), nullable=False)
    # isi = db.Column(db.String(1500), nullable=False)       
     
def TanyaAdd():
    try:
        isi = request.form.get('isi')
        googleuid = request.form.get('googleuid')

        inputs = [{
            'isi': isi,
            'googleuid': googleuid,
        }]

        tanyaAdd = Tanya(isi=isi, googleuid=googleuid, gambar_id=None)
        db.session.add(tanyaAdd)
        db.session.commit()

        return response.success(inputs, 'Sukses Menambahkan Pertanyaan')
    except Exception as e:
        print(e)
        
def TanyaAdd():
    try:
        output = request.get_json()
        isi = output['isi']
        googleuid = output['tanya_id']
        # gambar_id = None
        
        print(isi, googleuid)

        tanyaAdd = Tanya(isi=isi, googleuid=googleuid, gambar_id=None)
        db.session.add(tanyaAdd)
        db.session.commit()

        return response.success(output, 'berhasil tambah pertanyaan')
    except Exception as e:
        print(e)