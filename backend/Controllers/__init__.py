from Controllers.Dashboard import DashboardApi
from Controllers.Downloads import DownloadsApi
from Controllers.Cli import CommandsCli

def initialize(appl):
    # Register web api handlers
    appl.register_blueprint(DownloadsApi)
    appl.register_blueprint(CommandsCli)
