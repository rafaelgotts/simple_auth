# coding: utf-8

from flask import Flask

# Import do gerenciador de login Flask-Login. Sério!?
from flask.ext.login import LoginManager

"""
    Criando o gerenciador de login para adicionar a aplicação.
"""
login_manager = LoginManager()
"""
    Define o nível de proteção da sessão entre basic, strong e 
    None, que desativa a proteção.
"""
login_manager.session_protection = "strong"
"""
    Como definimos o prefix auth no blueprint, ele tem de ser 
    adicionado junto a view.
"""
login_manager.login_view = "auth.login"



"""
   Demorei uma cara pra perceber que esse método é necessário. 
   Como no manager ele usa o "app" para criar um novo objeto, eu
   demorei pra perceber que como antes o método create_app é usado
   o resultado é um objeto flask, e não o módulo app.
"""
def create_app():

    app = Flask(__name__)

    # Inicializando o flask-login no "factory" da aplicação.
    login_manager.init_app(app)

    # Import do blueprint para add a aplicação.
    from .auth import auth as auth_blueprint
    """
        O url_prefix é opcional, mas se definido fará com que 
        os urls do blueprint, tenham um prefixo.
    """
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app