
from graphviz import *
import csv

dot = Graph(engine='neato')
dot.node_attr.update(color='lightblue2', style='filled',  width='.025', height='.015', fontsize="6", margin="0,0")
dot.graph_attr.update(size="1000,1000", outputorder="edgesfirst")
dot.edge_attr.update(penwidth="0.3")

with open('node.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    node_list = []
    for row in csv_reader:
    	node_list.append(row)

for i in range(1, len(node_list)):
	node = str(node_list[i])
	dot.node(str(i - 1), node[2:-2])

with open('edges.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    edge_list = []
    for row in csv_reader:
    	edge_list.append(row)

for j in range(1, len(edge_list)):
	dot.edge(edge_list[j][0], edge_list[j][1], constraint='false')

dot.render('test-output/round-table.gv', view=True)