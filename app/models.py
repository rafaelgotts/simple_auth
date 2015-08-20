# coding: utf-8

# models.py
# Retirado do livro Flask Web Development, do Miguel Grinberg
# 2015.08.18

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """
           Classe que será usada para os usuários que 
        autenticarão na aplicação.

        __tablename__
              O SQLAlchemy definirá um nome para a tabela se 
            essa variável for omitida, porém ele não utiliza 
            a convenção de plural para o nome das tabelas.



        ## Métodos necessários na classe User para o uso do 
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

        ## Os métodos, password(os dois), e verify_password
        criam uma barreia maior de segurança ao seu sistema.
           O decorator @property, faz com que seja levantada
           uma exceção ao chamar a propriedade, e não exibe 
           o seu valor. Junto a isso, o setter da propriedade
           é "sobreescrito", fazendo com que seja salvo na
           variável de objeto password_hash, depois de ser
           criptografada pelo método generate_password_hash.
           Assim, ao definir um valor a password, só será
           possível ver o seu valor codificado, chamando o
           atributo self.password_hash.

    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        """
            Define password como um atributo, que só pode ser 
            adicionado um valor, não "exibido".
        """
        raise AttributeError('password não é um atributo legível')

    @password.setter
    def password(self, password):
        """
            Faz com que a seja salvo apenas uma hash da senha informada.
            Junto com o método que usa o decorator @property, passa a ser
            um atributo de classe, mas que não pode ter o seu valor exibido.
        """
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        """
            Verifica se a senha informada é igual a versão em hash 
            do objeto. Caso seja, retornará True.
        """
        return check_password_hash(self.password_hash, password)

