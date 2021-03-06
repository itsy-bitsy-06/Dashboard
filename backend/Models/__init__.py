import os
import json

from Models.DbRef import db, ma
from Models.JirasModel import JirasModel, JirasSchema
from Models.SeedsModel import ResetOrSeedDb

def initialize(appl):
    os.makedirs('./Data', exist_ok=True)
    db.init_app(appl)
    ma.init_app(appl)
    with appl.app_context():
        db.create_all()

__all__ = ['initialize', 'JirasModel', 'JirasSchema']

