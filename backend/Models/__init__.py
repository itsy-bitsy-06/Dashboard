import os
import json

from Models.DbRef import db, ma
from Models.GroupsModel import GroupsModel, GroupsSchema
from Models.SeedsModel import ResetOrSeedDb

def initialize(appl):
    os.makedirs('./Data', exist_ok=True)
    db.init_app(appl)
    ma.init_app(appl)

__all__ = ['initialize', 'GroupsModel', 'GroupsSchema']

