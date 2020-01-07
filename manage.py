from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app.models import *
from app import create_app, db

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@app.errorhandler(404)
def page_not_found(error):
    '''404'''
    return 'page not'


if __name__ == '__main__':
    manager.run()
