from .dict_utils import extract_dict_fields


def get_user_inputs():
    user_inputs = dict()
    user_inputs['pregnancies'] = int(input("Digite quantas gravidezes teve: "))
    user_inputs['age'] = int(input("Digite a sua idade: "))
    user_inputs['weight'] = float(input("Digite o seu peso: "))
    user_inputs['height'] = float(input("Digite a sua altura: "))
    user_inputs['bmi'] = calculate_bmi(user_inputs)
    print(f'O IMC calculado é de: {user_inputs["bmi"]}')
    user_inputs['blood_press'] = int(input("Digite a pressão coletada: "))
    user_inputs['glucose'] = int(input("Digite o índice glicêmico coletado: "))

    return user_inputs


def parse_request_data(request_form):
    weight = float(request_form['weight'])
    height = float(request_form['height'])
    return {
        'pregnancies': int(request_form['pregnancies']),
        'age': int(request_form['age']),
        'weight': weight,
        'height': height,
        'bmi': calculate_bmi(weight, height),
        'blood_press': int(request_form['blood_press']),
        'glucose': int(request_form['glucose'])
    }


def calculate_bmi(weight, height):
    return round((weight / (height ** 2)), 1)


def generate_dataset_from_input(inputs):
    pregnancies, glucose, bmi, blood_press, age = (
        extract_dict_fields(inputs, ['pregnancies', 'glucose', 'bmi', 'blood_press', 'age'])
    )
    return [[pregnancies, glucose, bmi, blood_press, age]]

