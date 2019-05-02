from operator import itemgetter


def extract_dict_fields(some_dict, fields):
    return itemgetter(*fields)(some_dict)
