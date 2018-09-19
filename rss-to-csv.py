
# guardian.py

# import packages
import json
import csv
from collections import OrderedDict

# Change JSON input file here!
with open('guardian-sept.json', 'r') as json_file:
	json_string = json_file.read()

parsed_json = json.loads(json_string.encode('utf-8').decode('utf-8-sig'))

# NODE LIST

category_list = []

# Create list of all categories
for i in range(0, len(parsed_json["items"])):
	for j in range(0, len(parsed_json["items"][i]["categories"])):
		category_list.append(parsed_json["items"][i]["categories"][j])

#Remove duplicates
categories = ["Label"]
node_list = []
for m in category_list:
	if m not in categories:
		categories.append(m)

with open('node.csv', 'w', newline='') as node_file:
	nodewriter = csv.writer(node_file, delimiter=',')

	count = -1
	for p in categories:
		nodewriter.writerow([p])
		if count >= 0:
			node_list.append([count, p])
		count += 1

# EDGE LIST

full_edge_list = []
weighted_edge_list = [["Source", "Target", "Weight"]]

for i in range(0, len(parsed_json["items"])):
	short_list = []

	# For each category in a news article
	for j in range(0, len(parsed_json["items"][i]["categories"])):
		for k in range(0, len(node_list)):
			if node_list[k][1] == parsed_json["items"][i]["categories"][j]:
				source_id = node_list[k][0]
				short_list.append(source_id)

	# For the list of category ids for an article
	for m in range(0, len(short_list)):

		source_category = short_list[m]
		count = m + 1

		while count < len(short_list):
			full_edge_list.append([source_category, short_list[count], 1])
			count += 1


# Calculate weights - GEPHI DOES THIS FOR YOU
"""
for m in full_edge_list:
	if m not in weighted_edge_list:
		weighted_edge_list.append([m[0], m[1], 1])
		print(m)
	elif m in weighted_edge_list:
		print(m)
		for n in weighted_edge_list:
			if n[0] == m[0] & n[1] == m[1]:
				n[2] += 1

print(weighted_edge_list)
"""

with open('edges.csv', 'w', newline='') as edge_file:
	edgewriter = csv.writer(edge_file, delimiter=',')
	edgewriter.writerow(["Source", "Target", "Weight"])
	for p in full_edge_list:
		edgewriter.writerow(p)


"""
# Create list of all categories
for i in range(0, len(parsed_json["items"])):
	for j in range(0, len(parsed_json["items"][i]["categories"])):
		category_list.append(parsed_json["items"][i]["categories"][j])

# Count appearance of each category
for i in range(0, len(category_list)):
	chosen_word = category_list[i]
	category_count.append([category_list[i], 1])

	for word in category_list:
		if chosen_word == word:
			category_count[i][1] += 1
"""


#print (edge_list)

# 		for k in range(0, 1):
#			if parsed_json["items"][i]["categories"][j] == category_list[k][0]:
#				category_list[k][1] += 1
#			else:
#				category_list.append([parsed_json["items"][i]["categories"][j], 1])