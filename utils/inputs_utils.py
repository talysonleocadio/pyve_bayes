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


def calculate_bmi(inputs, fields=['height', 'weight']):
    height, weight = extract_dict_fields(inputs, fields)
    return round((weight / (height ** 2)), 1)


def get_user_inputs_dataset(inputs):
    pregnancies, glucose, bmi, blood_press, age = (
        extract_dict_fields(inputs, ['pregnancies', 'glucose', 'bmi', 'blood_press', 'age'])
    )
    return [[pregnancies, glucose, bmi, blood_press, age]]

