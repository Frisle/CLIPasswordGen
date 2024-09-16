import json
import dropbox_IO_module as dropbox_upload

def create_pass_json(json_db, initial_structure):
    with open(json_db, "w", encoding="utf-8") as json_file:
        if initial_structure:
            json_object = json.dumps(initial_structure, indent=4)
        else:
            json_object = json.dumps({}, indent=4)
        json_file.write(json_object)


def check_create_data_base(json_db, initial_structure=""):
    try:
        file = open(json_db, "r")
        file.close()
    except FileNotFoundError:
        create_pass_json(json_db, initial_structure)


def read_json(file_name, position="", printing=False):

    """
    Simple read and return function.
    Read one particular upper lever position
    :param position: key of the dict
    :param file_name: dict file name
    :param printing: print the resul of reading or not
    :return: json: any data that held in the file
    """

    def print_result(data):
        if printing:
            print(json.dumps(data, indent=2))
        else:
            return

    with open(file_name, "r") as json_file:
        file_data = json.load(json_file)
        if position:
            data_pull = file_data[position]
            print_result(data_pull)
            return data_pull
        else:
            print_result(file_data)
            return file_data


def append_data_json(position, data, file_name):
    with open(file_name, "r") as json_file:
        file_data = json.load(json_file)

    file_data[position].append(data)

    with open(file_name, "w") as json_file:
        json.dump(file_data, json_file, ensure_ascii=False, indent=4)
    dropbox_upload.upload_password()


def update_dict(data, file_name):
    with open(file_name, "r") as json_file:
        file_data = json.load(json_file)

    file_data.update(data)
    
    with open(file_name, "w") as json_file:
        json.dump(file_data, json_file, ensure_ascii=False, indent=4)


