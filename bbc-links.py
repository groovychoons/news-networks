
# bbc.py

# import packages
import json
import csv

with open('bbcuk.json', 'r') as json_file:
	json_string = json_file.read()

parsed_json = json.loads(json_string.encode('utf-8').decode('utf-8-sig'))

# LIST OF LINKS
link_list = []

# Create list of all links
for i in range(0, len(parsed_json["items"])):
	link_list.append(parsed_json["items"][i]["link"])

with open('bbclinks.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=',')

	for p in link_list:
		writer.writerow([p])




