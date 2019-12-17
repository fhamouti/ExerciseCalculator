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

#Get data into json string
json_str = json.dumps(data, indent=4)

#Convert json string into json list
json_list = json.loads(json_str)

#Open file to write logs and append to actual info
logs = open("operation_logs.txt", "a")

for element in json_list:
    #print(element)
    res = requests.post('http://localhost:5000/', json=element)

    #Show response from server
    print(res.text)
    
    #Write response in a file
    logs.write(res.text+'\n')

#Close file after finishing writing
logs.close()