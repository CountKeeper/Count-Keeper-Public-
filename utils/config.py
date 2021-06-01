import json
with open("CountKeeperData/config.json") as json_config_file:
    configData = json.load(json_config_file)
    print("Config file read")
    json_config_file.close()
for key, value in configData.items():
    #Loads everything in configData into global variables. Makes using config.py less implementation dependent
    globals()[key] = value