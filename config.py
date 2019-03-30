import json 

with open('config.json') as json_data_file:
    config = json.load(json_data_file)
SOURCE_CODE_FILEPATH = config["source_code_filepath"]