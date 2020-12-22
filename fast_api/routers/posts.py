from fastapi import APIRouter, Body

from bson.objectid import ObjectId
from bson.json_util import dumps, loads

from database import db

router = APIRouter()
@router.post('')
def create_post(body=Body(...)):
    """postの作成

    ----------
    Parameters:

    body: body
        任意のjson
    """
    post = body['payload']
    db.posts.insert(post)
    return {'post': "ok"}

@router.get('')
def read_post():
    """postの取得

    ----------
    Parameters:

    なし
    """
    db_post = db.posts.find_one()
    return {'item': dumps(db_post)}

@router.get('/{id}')
def read_post_by_id(id: str):
    """postの取得(id)

    ----------
    Parameters:

    id: str
        オブジェクトID
    """
    db_post = db.posts.find_one({'_id': ObjectId(id)})
    return {'item': dumps(db_post)}

@router.put('')
def update_post(body=Body(...)):
    """postの更新(id)

    ----------
    Parameters:

    id: str
        オブジェクトID
    """
    post = body['payload']
    _id = post['_id']
    print(_id)
    title = post['title']
    text = post['text']
    db.posts.update_one(
        {'_id': ObjectId(_id)},
        {'$set':
            {
                "title": title, 'text': text
            }
        }
    )
    return {'update': "ok"}

@router.delete('/')
def delete_post_by_id(id: str):
    """postの削除(id)

    ----------
    Parameters:

    id: str
        オブジェクトID
    """
    db.posts.delete_one(
        {'_id': ObjectId(id)}
    )
    return {'delete': "ok"}
