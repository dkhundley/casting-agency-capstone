from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import APP
from models import casting_db

migrate = Migrate(APP, casting_db)
manager = Manager(APP)

manager.add_command('casting_db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
