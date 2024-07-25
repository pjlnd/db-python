from peewee import *

db = SqliteDatabase('usuarios.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db