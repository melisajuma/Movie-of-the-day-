from app import create_app, db
from flask_script import Manager,Server
from app.models import *
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance


manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db=db, User=User, Genres= Genres)


if __name__ == '__main__':
    manager.run()
