import os
import time
import datetime
from collections import OrderedDict
from flask import Blueprint, request
from flask_restful import Resource
from werkzeug import secure_filename
from Models import JirasModel, JirasSchema
from Library.Client.Stats import Excel

from Controllers.ApiRef import RootApi


class DashboardController(Resource):
    def get(self):
        jiras = JirasModel.query.filter().all()
        schema = JirasSchema(many=True)
        return schema.dump(jiras)

    def put(self):
        """ Updates the remote refs  """
        return {}

    def post(self):
        file = request.files['file']
        filename = os.path.join('./Workspace', secure_filename(file.filename))
        file.save(filename)
        df = Excel.ReadExcel(filename)
        schema = JirasSchema(many=True)
        jiras = schema.load(df)
        list(map(lambda x: x.insert(), jiras))
        return schema.dump(jiras)

DashboardApi = Blueprint('Dashboard', __name__, url_prefix='/api/dashboard')
__api = RootApi(DashboardApi)
__api.add_resource(DashboardController, '')
