# -*- encoding: utf-8 -*-


"""
   O método create_app é usado apenas porque ele 
   retornará um objeto flask, mas não recebe nenhum
   argumento atualmente.
"""
from app import create_app

"""
    Importa a classe Manager, dos scripts padrões do flask.
    Com o objeto desta classe que nós poderemos gerenciar tudo!
"""
from flask.ext.script import Manager

app = create_app()
manager = Manager(app)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    manager.run()