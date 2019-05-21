from flask import render_template, request, redirect, url_for
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/predict', methods=['POST'])
def predict_from_user_data():
    user_inputs = request.form.to_dict()
    return(f'{user_inputs}')
