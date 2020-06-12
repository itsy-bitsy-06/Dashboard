import csv
import click
from zipfile import ZipFile
from flask import Blueprint
from tabulate import tabulate

from Library.Client import Groups
# https://stackoverflow.com/a/58276955

CommandsCli = Blueprint('cli', __name__)

@CommandsCli.cli.command('ShowGroups')
def show_groups():
    """ flask cli ShowGroups """
    ignores = ['systems', 'updated', 'created', 'tasks']
    groups = Groups.get_all()
    list(map(lambda x: [x.pop(i) for i in ignores], groups)) # remove columns we dont want in output
    align= ['right'] * 6 # 6 columns
    print(tabulate(groups, headers='keys', tablefmt='github', colalign=align))


@CommandsCli.cli.command('Restore')
@click.argument('file')
def restore_systems(file):
    """ flask cli Restore backup.zip"""
    with ZipFile(file) as backup:
        groupbk = backup.open('groups.csv')
        for row in groupbk:
            id, name, description, os, username, password=row.decode('utf-8').strip().split(',')
            payload = dict(name=name, description=description, username=username, password=password, os=os)
            Groups.create(payload)
        groupbk.close()
        systembk = backup.open('systems.csv')
        for row in systembk:
            id, name, ip, group_id = row.decode('utf-8').strip().split(',')
            Systems.add(name, ip, group_id, id)
        systembk.close()
        print(f'Restored Group and System from archive: {file}')

