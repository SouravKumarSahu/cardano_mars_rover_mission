def write_output_text(file_name, rovers, json):
    with open(file_name, 'w') as f:
        f.write(str(json['grid'][0]) + " " + str(json['grid'][1]) + "\n")
        for rover in rovers:
            f.write(rover.__str__() + "\n" + rover.status +
                    " - (" + rover.message + ")\n")
