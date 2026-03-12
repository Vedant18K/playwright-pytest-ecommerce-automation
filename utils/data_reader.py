import json


def load_test_data(filepath):
    with open(filepath) as file:
        return json.load(file)
