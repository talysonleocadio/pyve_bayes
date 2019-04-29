from sklearn.naive_bayes import MultinomialNB


def create_model():
    return MultinomialNB()


def fit_model(data_dict, model):
    inputs, output = data_dict
    model.fit(inputs, output)


def predict_model(new_contract, model):
    return model.predict(new_contract)

