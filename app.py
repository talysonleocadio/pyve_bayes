from utils.file_utils import (
    get_dirt_file_path, get_sanitized_file_path, file_exists)
import datasets.dataset as ds
import bayes.classifier_nb as classifier
from configs.config_utils import get_configs
from operator import itemgetter

dirt_file_path = get_dirt_file_path()
sanitized_file_path = get_sanitized_file_path()
replace_properties, model_proprerties = (
    itemgetter('replace_properties', 'model_properties')(get_configs()))

if (not file_exists(sanitized_file_path)):
    dataset = ds.generate_dataset(dirt_file_path)
    ds.sanitize_dataset(dataset, replace_properties)
    ds.generate_sanitized_csv(dataset, sanitized_file_path)
else:
    dataset = ds.generate_dataset(dirt_file_path)

inputs, output = ds.extract_model_propeties(dataset, model_proprerties)

model = classifier.create_model()
