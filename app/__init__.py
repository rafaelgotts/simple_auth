# coding: utf-8

from flask import Flask


"""
   Demorei uma cara pra perceber que esse método é necessário. 
   Como no manager ele usa o "app" para criar um novo objeto, eu
   demorei pra perceber que como antes o método create_app é usado
   o resultado é um objeto flask, e não o módulo app.
"""
def create_app():

    app = Flask(__name__)

    return app