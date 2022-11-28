from app.model.post import Post
from app.model.tanya import Tanya 

from app import response, app, db
from flask import request

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
        'judul' : post.judul,
        'isi' : post.isi,
        'gambar_id' : post.gambar_id,
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

    
