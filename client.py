import csv
import json
import requests

#Init variables 
data = []
json_str = {}

#Name of attributes
fieldnames = ('value1','operation','value2')

#Get info from csv file
with open('sample.csv') as f:
    for row in csv.DictReader(f,fieldnames):
        data.append(row)

#Get data 
json_data = json.dumps(data, indent=4)

#Send POST
res = requests.post('http://localhost:5000/', json=json_data)

