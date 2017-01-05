# app.py

import peewee
from ray_peewee.all import PeeweeModel
from ray.wsgi.wsgi import application
from ray.endpoint import endpoint

database = peewee.SqliteDatabase('example.db')

class DBModel(PeeweeModel):
    class Meta:
        database = database

@endpoint('/post')
class Post(DBModel):
    title = peewee.CharField()
    text = peewee.CharField()

if __name__ == '__main__':
    database.connect()
    database.create_tables([Post], safe=True)
    database.close()
    application.run(debug=True, reloader=True)

