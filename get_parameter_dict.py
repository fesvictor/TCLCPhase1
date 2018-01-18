def get_parameter_dict():
    import os
    this_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(this_folder, 'parameter-file.txt')
    parameter_dict = {}
    with open(file_name) as file:
        for row in file:
            if row[0] is not "#" and row[0] is not "\n" and row[0] is not " ":
                row = row.replace("\n", "").split("=")
                parameter_dict[row[0]] = row[1]
    return parameter_dict
