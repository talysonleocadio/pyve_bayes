import pandas as pd
from utils.dict_utils import extract_dict_fields


def get_dataset_from_file(file_path):
    return pd.read_csv(file_path, sep=',')


def extract_model_propeties(dataset, propeties_dict):
    inputs, output = extract_dict_fields(propeties_dict, ['inputs', 'output'])
    return dataset[inputs], dataset[output]
