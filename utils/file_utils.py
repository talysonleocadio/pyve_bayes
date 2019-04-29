import os
from configs import get_configs
from operator import itemgetter

loaded_json = get_configs()

sanitized_file, dirt_file = (
    itemgetter('sanitized_file', 'dirt_file')(loaded_json))


def get_sanitized_file_path():
    return f'{os.getcwd()}/{sanitized_file}'


def get_dirt_file_path():
    return f'{os.getcwd()}/{dirt_file}'


def file_exists(file_path):
    return os.path.exists(file_path)
