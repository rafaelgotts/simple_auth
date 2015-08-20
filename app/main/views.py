# coding: utf-8

from flask import render_template
from flask.ext.login import login_required

# Importa o blueprint main
from . import main

# import ipdb; ipdb.set_trace()
# Cria uma rota no blueprint para /login
@main.route("/secret")
@login_required
def secret():
    import ipdb; ipdb.set_trace()
    return "Apenar usuário autenticado!"