
import datetime
from Models.DbRef import db, ma
from marshmallow import pre_dump


class GroupsModel(db.Model):
    __tablename__ = 'Groups'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)       # Name of this group
    description = db.Column(db.String(255))                             # Description for this group
    os = db.Column(db.String(16), default='Windows')                    # Windows Linux OsX
    username = db.Column(db.String(32), nullable=False)                 # Username for this group
    password = db.Column(db.String(32), nullable=False)                 # Username for this group
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)  # Creation time
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)  # Updation time

    def insert(self):
        self.updated = datetime.datetime.utcnow()
        db.session.add(self)
        db.session.commit()

class GroupsSchema(ma.ModelSchema):
    class Meta:
        model = GroupsModel
        sqla_session = db.session
        include_fk = True
        strict = True

    @pre_dump
    def pre_process(self, data, many=False):
        # Dont include tasks launched for a parallel of the group.
        tasks = list(filter(lambda x: x.parallel is False, data.tasks))
        # Dont include tasks that are waiting in queue
        tasks = list(filter(lambda x: x.status not in ['QUEUED', 'ABORTED'], tasks))
        data.tasks = tasks
        return data