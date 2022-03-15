
# JSON READER
import json
def read_dare_json():
    with open("dare_list.json", 'r') as json_file:
        json_string = json_file.read()
        dare_list = json.loads(json_string)

    return dare_list

def read_truth_json():
    with open("truth_list.json", 'r') as json_file:
        json_string = json_file.read()
        truth_list = json.loads(json_string)
    return truth_list

