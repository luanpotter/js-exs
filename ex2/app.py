# app.py

import peewee
import json
from playhouse.shortcuts import model_to_dict
from ray_peewee.all import PeeweeModel
from ray.wsgi.wsgi import application
from ray.endpoint import endpoint
from ray.actions import Action, action
from bottle import static_file

database = peewee.SqliteDatabase('example.db')

class DBModel(PeeweeModel):
    class Meta:
        database = database

@endpoint('/post')
class Post(DBModel):
    title = peewee.CharField()
    likes = peewee.IntegerField(default=0)

class PostActions(Action):
    __model__ = Post

    @action('/<id>/like')
    def like(self, post_id, params):
        post = Post.select().where(Post.id == post_id)[0]
        post.likes = post.likes + 1
        post.update()
        return model_to_dict(post)

if __name__ == '__main__':
    database.connect()
    database.create_tables([Post], safe=True)
    database.close()
    application.run(debug=True, reloader=True)

@application.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

