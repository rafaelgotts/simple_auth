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
    Aqui você define qual view será direcionado o usuário que
    não estiver logado.
    Como definimos o prefix auth no blueprint, ele tem de ser 
    adicionado junto a view.

    ATENÇÃO!
    Ao adicionar uma view de login ao login_manager, o flask
    fará um redirecionamento e passará informações de sessão.
    Caso vocẽ não tenha configurado a SECRET_KEY, o flask não
    irá funcionar e irá retornar um erro 500 bem bonito pra
    você.
"""
login_manager.login_view = "auth.login"


from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

"""
   Demorei uma cara pra perceber que esse método é necessário. 
   Como no manager ele usa o "app" para criar um novo objeto, eu
   demorei pra perceber que como antes o método create_app é usado
   o resultado é um objeto flask, e não o módulo app.
"""
def create_app():

    app = Flask(__name__)

    """
        Adicionado apenas por causa do redirect que o login_manager
        faz, e caso não tenha uma SECRET_KEY, poderá não funcionar.
    """
    app.config["SECRET_KEY"] = "dificil de advinhar que era isso"

    """
        Inicializando as extensões da aplicação.
        Descobri que o "factory" da aplicação é nada mais, nada 
        menos que esse método (create_app). :D
    """
    login_manager.init_app(app)
    db.init_app(app)

    """
        Importando o blueprint para registrá-lo na aplicação.
        O url_prefix é opcional, mas se definido fará com que 
        os urls do blueprint, tenham um prefixo.
    """
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")


    # LINHAS DESCARTÁVEIS
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # app.debug = True

    return app