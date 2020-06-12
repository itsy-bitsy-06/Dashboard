from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

class SQLiteAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        options.update({
            'isolation_level': None
        })
        super(SQLiteAlchemy, self).apply_driver_hacks(app, info, options)


db = SQLiteAlchemy(session_options={'autoflush': False, 'autocommit': False, 'expire_on_commit': False })
ma = Marshmallow()
