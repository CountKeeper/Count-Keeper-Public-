import json
with open("config.json") as json_config_file:
    configData = json.load(json_config_file)
    print("Config file read")
    json_config_file.close()