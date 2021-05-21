from json import loads


def write_output_text(file_name, json_output):
    dict_output = loads(json_output)
    with open(file_name, 'w') as f:
        f.write(str(dict_output['grid'][0]) + " " +
                str(dict_output['grid'][1]) + "\n")
        for rover in dict_output['rovers']:
            f.write(rover[0] + "\n" + rover[1] + "\n")
