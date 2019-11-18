import csv, json

csvFilePath = 'data5.csv'
jsonFilePath = 'convert.json'

csvfile = open(csvFilePath, 'r')
jsonfile = open(jsonFilePath, 'w')


fieldnames=("Event name", "Device ID", "Call ID", "Partner ID", "Code" , "Data")

reader = csv.DictReader( csvfile, delimiter='\t')
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

csvfile.close()
jsonfile.close()
