from peewee import *

arq = './database.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    cliente_nome = CharField()
    cliente_endereco = CharField()
    cliente_telefone = CharField()

class Produto(BaseModel):
    produto_nome = CharField()
    produto_valor = DecimalField()
    produto_descricao = CharField()

class Pedido(BaseModel):
    pedido_cliente = ForeignKeyField(Cliente, backref='cliente')
    pedido_produto = ForeignKeyField(Produto, backref='produto')   


if __name__ == "__main__":
    db.connect()
    db.create_tables([Cliente, Produto, Pedido])
