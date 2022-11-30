from app.model.post import Post
from app.model.tanya import Tanya 

from app import response, app, db
from flask import request, jsonify


def PostList():
    try:
        post = Post.query.all()
        data = transform(post)
        return response.success(data, "Data berhasil didapatkan")
    except Exception as e:
        print(e)
                
def transform(datas):
    array = []
    
    for i in datas:
        array.append(singleTransform(i))
    return array

def singleTransform(data):
    data = {
        'id' : data.id,
        'isi' : data.isi,
        'tanya_id' : data.tanya_id,
        # 'gambar_id' : post.gambar_id,
    }
    return data


def PostbyID(id):
    try:
        posts = Post.query.filter_by(id=id).first()
        data = singleTransform(posts)
        return response.success(data, "Data berhasil didapatkan")
    
    except Exception as e:
        print(e)

def PostAdd():
    try:
        output = request.get_json()
        isi = output['isi']
        tanya_id = output['tanya_id']
        
        postAdd = Post(isi = isi, tanya_id = tanya_id)
        db.session.add(postAdd)
        db.session.commit()

        return response.success(output, 'ini output')
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
    
