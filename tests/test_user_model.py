# coding: utf-8

# testing.py
# Retirado do livro Flask Web Development, do Miguel Grinberg
# 2015.08.18

import unittest

"""
   O import está sendo direto, e não criando através
   do método create_app, pois ele não existe no __init__
   do módulo app. Será usado assim por motivos de 
   simplicidade.

   Isso implica que sempre será o mesmo ENVIRONMENT, e que
   se for usado para outro propósito que não estudo/teste,
   deverá ser criado da forma correta, com o método e tudo
   mais.
"""
import app


from app.models import User

class UserModelTestCase(unittest.TestCase):

    
    def test_password_setter(self):
        u = User(password = 'cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password = 'cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)