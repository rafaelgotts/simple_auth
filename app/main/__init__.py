# coding: utf-8

"""
    Deixando o app main como um Blueprint, o que 
    facilitará depois para adicioná-lo em outro projeto
"""
from flask import Blueprint

"""
    Cria o objeto Blueprint com o nome main e __name__
    que eu AINDA não entendi. Mas eu conseguirei. XD
"""
main = Blueprint('main', __name__)

"""
    Import do próprio módulo views, permitindo o acesso
    depois a esse mesmo módulo, pelo Blueprint.
"""
from . import views