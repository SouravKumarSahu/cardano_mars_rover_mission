from json import dumps


def read_input_text(file_name):
    dict_input = {}
    with open(file_name, 'r') as f:
        dict_input['grid'] = [int(k) for k in f.readline().split()]
        dict_input['instructions'] = []
        for l in f:
            dict_input['instructions'].append(
                [l.split(), f.readline().split()])
    return dumps(dict_input)
