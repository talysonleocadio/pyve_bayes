import os
import json

PATH = os.path.dirname(os.path.realpath(__file__))


def get_configs(conf_list=[]):
    with open(f'{PATH}/constants.json', 'r') as conf_file:
        return json.load(conf_file)
