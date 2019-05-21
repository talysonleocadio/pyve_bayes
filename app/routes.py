from flask import render_template, request, redirect, url_for
from app import app
from utils.inputs_utils import parse_request_data, generate_dataset_from_input
import bayes.classifier_nb as classifier
from utils.file_utils import get_dataset_file_path
import datasets.dataset as ds
from configs.config_utils import get_configs
from utils.dict_utils import extract_dict_fields


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/predict', methods=['POST'])
def predict_from_user_data():
    parsed_request = parse_request_data(request.form.to_dict())
    input_dataset = generate_dataset_from_input(parsed_request)

    dataset_file_path = get_dataset_file_path()
    dataset = ds.get_dataset_from_file(dataset_file_path)

    loaded_json = get_configs()
    model_properties = extract_dict_fields(loaded_json, ['model_properties'])
    inputs, output = ds.extract_model_propeties(dataset, model_properties)

    model = classifier.create_model()
    model.fit(inputs, output.values.ravel())
    prediction = model.predict(input_dataset)

    return(render_template(
        'prediction.html', title='Predict',
        predict=prediction[0], bmi=parsed_request['bmi']))
