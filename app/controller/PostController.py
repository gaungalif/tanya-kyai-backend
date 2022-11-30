from app.model.post import Post
from app.model.tanya import Tanya 

from app import response, app, db
from flask import request
    # id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    # isi = db.Column(db.String(1500), nullable=False)
    # tanya_id = db.Column(db.BigInteger, db.ForeignKey('tanya.id'), nullable=True)
    # # gambar_id = db.Column(db.BigInteger, db.ForeignKey('gambar.id'), nullable=True)
def PostList():
    try:
        posts = Post.query.all()
        data = transform(posts)
        return response.success(data, "Data berhasil didapatkan")
    except Exception as e:
        print(e)
                
def singleTransform(post):
    data = {
        'id' : post.id,
        'isi' : post.isi,
        # 'gambar_id' : post.gambar_id,
        'tanya_id' : post.tanya_id
    }
    return data

def transform(posts):
    array = []
    for i in posts:
        array.append(singleTransform(i))
    return array


def PostbyID(id):
    try:
        posts = Post.query.filter_by(id=id).first()
        data = singleTransform(posts)
        return response.success(data, "Data berhasil didapatkan")
    
    except Exception as e:
        print(e)

def PostAdd():
    try:
        isi = request.form.get('isi')
        # tanya_id = request.form.get('tanya_id')
        # gambar_id = request.form.get('gambar_id')

        inputs = [{
            'isi': isi,
            # 'tanya_id': tanya_id,
            # 'gambar_id': 1
        }]

        postAdd = Post(isi=isi)
        db.session.add(postAdd)
        db.session.commit()

        return response.success(inputs, 'Sukses Menambahkan Post')
    except Exception as e:
        print(e)
        
def PostDelete(id):
    try:
        post = Post.query.filter_by(id=id).first()
        if not post:
            return response.badRequest([], 'Data Dosen Kosong...')
        
        db.session.delete(post)
        db.session.commit()

        return response.success('', 'Berhasil menghapus data!')
    except Exception as e:
        print(e)
    
