
import json
import pandas as pd
with open('C:\\Users\\56932\\OneDrive\\Escritorio\\ejemplos de practica\\2022-01-05_090441.387603 (3).json') as data_file:
    data = json.loads(data_file.read())

for i in range(len(data["jams"])):
    print(i,data["jams"][i]["level"])

