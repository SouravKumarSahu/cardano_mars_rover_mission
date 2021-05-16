def read_input_text(file_name):
    json = {}
    with open(file_name, 'r') as f:
        json['grid'] = [int(k) for k in f.readline().split()]
        json['instructions'] = []
        for l in f:
            json['instructions'].append([l.split(), f.readline().split()])
    return json
