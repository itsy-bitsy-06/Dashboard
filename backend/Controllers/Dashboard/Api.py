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
        today = datetime.date.today() + datetime.timedelta(days=1)
        pass_history = OrderedDict()
        fail_history = OrderedDict()
        # for i in range(0, 8):
        #     past_a = today - datetime.timedelta(days=7 - i)
        #     past_b = today - datetime.timedelta(days=7 - i + 1)
        #     pass_history[ past_b.strftime("%d/%m") ] = ResultsModel.query.filter(ResultsModel.status.like('PASSED')).filter(ResultsModel.created.between(past_b, past_a)).with_entities(func.count(ResultsModel.id)).scalar()
        #     fail_history[ past_b.strftime("%d/%m") ] = ResultsModel.query.filter(ResultsModel.status.like('FAILED')).filter(ResultsModel.created.between(past_b, past_a)).with_entities(func.count(ResultsModel.id)).scalar()

        # result = {
        #     'week_pass': pass_history,
        #     'week_fail': fail_history,
        #     'version': version,
        #     'releases': tags
        # }
        return {'a' : 10}

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
        return schema.dump(jiras)

DashboardApi = Blueprint('Dashboard', __name__, url_prefix='/api/dashboard')
__api = RootApi(DashboardApi)
__api.add_resource(DashboardController, '')
