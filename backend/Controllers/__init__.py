import os
from Controllers.Dashboard import DashboardApi
from Controllers.Downloads import DownloadsApi

def initialize(appl):
    # Register web api handlers
    os.makedirs('./Workspace', exist_ok=True)
    appl.register_blueprint(DashboardApi)
    appl.register_blueprint(DownloadsApi)
