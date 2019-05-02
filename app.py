from utils.file_utils import get_dataset_file_path
import datasets.dataset as ds
import bayes.classifier_nb as classifier
from utils.inputs_utils import get_user_inputs, get_user_inputs_dataset
from configs.config_utils import get_configs
from utils.dict_utils import extract_dict_fields

dataset_file_path = get_dataset_file_path()
dataset = ds.get_dataset_from_file(dataset_file_path)

loaded_json = get_configs()
model_properties = extract_dict_fields(loaded_json, ['model_properties'])
inputs, output = ds.extract_model_propeties(dataset, model_properties)

model = classifier.create_model()
model.fit(inputs, output.values.ravel())

user_inputs = get_user_inputs()
input_dataset = get_user_inputs_dataset(user_inputs)

print(model.predict(input_dataset))

