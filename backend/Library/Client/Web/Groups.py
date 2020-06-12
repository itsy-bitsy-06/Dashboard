import requests
from Library.Client.Web.WebRef import Modelify

def create(payload, host="localhost"):
    group = requests.post(f'http://{host}:8000/api/groups', json=payload, verify=False)
    return Modelify(group.json())


def get_all(host="localhost"):
    groups = Modelify(requests.get(f'http://{host}:8000/api/groups', verify=False).json())
    return groups
