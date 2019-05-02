import os
from configs import get_configs
from .dict_utils import extract_dict_fields

loaded_json = get_configs()

dataset_file = (
    extract_dict_fields(loaded_json, ['dataset_file']))


def get_dataset_file_path():
    return f'{os.getcwd()}/{dataset_file}'


def file_exists(file_path):
    return os.path.exists(file_path)
