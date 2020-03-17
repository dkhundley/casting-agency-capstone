from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import casting_db

migrate = Migrate(app, casting_db)
manager = Manager(app)

manager.add_command('casting_db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
