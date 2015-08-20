# coding: utf-8

# simple_auth.py
# Rafael Gottsfritz
# 2015.08.18

# Imports do app
from flask import Flask

# Imports do model
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin


# Parametros do app
app = Flask(__name__)

# Parametros do model
db = SQLAlchemy()


# Classe do model... Sério???
class User(UserMixin, db.Model):

    """
           Classe que será usada para os usuários que 
        autenticarão na aplicação.

        __tablename__
              O SQLAlchemy definirá um nome para a tabela se 
            essa variável for omitida, porém ele não utiliza 
            a convenção de plural para o nome das tabelas.



        Métodos necessários na classe User para o uso do 
        Flask-Login:

        is_authenticated(): Que deverá retornar True se o
                            usuário tiver credenciais
                            válidas.

        is_active(): Que deverá retornar True se a conta
                     de usuário estiver ativa.

        is_anonymous(): Que deverá retornar True se o 
                        usuário atual for anônimo.

        get_id(): Ao enviar uma instância de User, retornará 
                  um ID único.



    """

    __tablename__ = 'users'

    email = db.Column(db.String(64), primary_key=True)
    password_hash = db.Column(db.String(128))
    authenticated = db.Column(db.Boolean, default=False)

    # def is_active(self):
    #     """
    #         Melhor deixar como True (hardcoded) até que
    #         exista uma forma de ativar/desativar.
    #     """
    #     return True

    # def is_anonymous():
    #     """
    #         Melhor deixar como False (hardcoded) até que
    #         exista uma forma de o usuário logar como 
    #         anônimo.
    #     """
    #     return False




@app.route("/restricted")
def restricted_page():
    return "<html><body><h1>Pagina restrita!</h1></body></html>"

if __name__ == "__main__":
    app.run(debug=True)