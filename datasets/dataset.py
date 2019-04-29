import pandas as pd
from operator import itemgetter


def generate_dataset(file_path):
    return pd.read_csv(file_path, sep=';')


def sanitize_dataset(dataset, replace_dict):
    dataset.replace(replace_dict, inplace=True)


def generate_sanitized_csv(dataset, file_path):
    dataset.to_csv(file_path, sep=';', encoding='utf_8')


def extract_model_propeties(dataset, propeties_dict):
    inputs, output = itemgetter('inputs', 'output')(propeties_dict)
    return dataset[inputs], dataset[output]
