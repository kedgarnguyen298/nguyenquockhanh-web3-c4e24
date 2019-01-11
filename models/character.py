from mongoengine import *

class Character(Document):
    name = StringField()
    image = StringField()
    rate = IntField()
    