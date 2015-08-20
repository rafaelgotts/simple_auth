# coding: utf-8

from flask import render_template

# Importa o blueprint auth
from . import auth

# Cria uma rota no blueprint para /login
@auth.route("/login")
def login():
    return render_template('auth/login.html')