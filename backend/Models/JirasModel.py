
from Models.DbRef import db, ma
from marshmallow import pre_dump, EXCLUDE

class JirasModel(db.Model):
    __tablename__ = 'Jiras'
    Key = db.Column(db.String(16), primary_key=True)                    # Key of this jira
    Status = db.Column(db.String(16), nullable=False)                   # Status of this jira
    Description = db.Column(db.String(2048))                            # Description for this group
    Created = db.Column(db.DateTime, nullable=False)                    # Creation time
    Duration = db.Column(db.Integer, default=0)                         # Time to Resolution
    IssueType = db.Column(db.String(16), nullable=False)                # Issue type
    CustomerRequestType = db.Column(db.String(16), nullable=False)      # Request Type
    Resolution = db.Column(db.String(16), nullable=False)               # Resolution

    def insert(self):
        db.session.add(self)
        db.session.commit()

class JirasSchema(ma.ModelSchema):
    class Meta:
        unknown = EXCLUDE
        model = JirasModel
        sqla_session = db.session
        include_fk = True
        strict = True
