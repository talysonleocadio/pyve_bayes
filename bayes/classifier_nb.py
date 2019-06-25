from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


def create_model():
    return MultinomialNB()


def fit_model(data_dict, model):
    inputs, output = data_dict
    model.fit(inputs, output)


def predict_model(new_contract, model):
    return model.predict(new_contract)


def splitting_dataset(dataset_inputs, dataset_outputs):
    inputs_fit, inputs_test, outputs_fit, outputs_test = (
        train_test_split(dataset_inputs,
                         dataset_outputs,
                         test_size=0.30)
    )
    return {
        'fit': {
            'inputs': inputs_fit,
            'outputs': outputs_fit
        },
        'test': {
            'inputs': inputs_test,
            'outputs': outputs_test
        }
    }


def get_confusion_matrix(test_outputs, predicted_test_outputs):
    return confusion_matrix(test_outputs, predicted_test_outputs).ravel()


def get_metrics(confusion_matrix):
    TN, FP, FN, TP = confusion_matrix

    return {
        'accuracy': (TP + TN) / float(TP + TN + FP + FN),
        'error': (FP + FN) / float(TP + TN + FP + FN),
        'sensivity': TP / float(FN + TP),
        'specificity': TN / float(TN + FP)
    }

