

## NLP part
import gensim
from gensim import corpora
from pprint import pprint  # pretty-printer
import csv

documents = []

# import data
for  count in range(0,66):
	file = open("BBC/bbcnewsdata%s.txt" % count, "r")
	documents.append(file.read())

# remove common words and tokenize
stoplist = set("}); && { } []  - 0 1 2 3 4 5 6 7 8 9 ms mr mrs also just says share image will not said a about above after again against all am an and any are as at be because been before being below between both but by could did dick do does doing down during each few for from further had has have having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've i\'ve if in into is it it's its itself let's me more most my myself nor of on once only or other ought our ours ourselves out over own same she she'd she'll she's should so some such than that that's the their theirs them themselves then there there's these they they'd they'll they're they've this those through to too under until up very was we we'd we'll we're we've were what what's when when's where where's which while who who's whom why why's with would you you'd you'll you're you've your yours yourself yourselves".split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]

# create dictionary
dictionary = corpora.Dictionary(texts)
dictionary.save('bbc.dict')

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('bbc.mm', corpus) #stores to disc
mm = gensim.corpora.MmCorpus('bbc.mm')

lsi = gensim.models.lsimodel.LsiModel(corpus=mm, id2word=dictionary)
topic_string = lsi.show_topics()

pprint(topic_string)
pprint('========')

## Create nodes and edges list

import re

# Gets topics in a nice list
def cleantopics(raw_string):
	cleanr = re.compile('"[^"]+"')
	cleantext = re.findall(cleanr, raw_string)
	count = 0
	for word in cleantext:
		cleantext[count] = word[1:-1]
		count += 1
	return cleantext


c_topics = cleantopics(str(topic_string))

# Gets 10 topics for each article in their own list

topics = []
little_list = []

for i in range(0, len(c_topics)):
	little_list.append(c_topics[i])

	if i % 10 == 0 and i != 0:
		topics.append(little_list)
		little_list = []


categories = ["Label"]
node_list = []
for m in c_topics:
	if m not in categories:
		categories.append(m)

with open('node.csv', 'w', newline='') as node_file:
	nodewriter = csv.writer(node_file, delimiter=',')

	count = -1
	for p in categories:
			nodewriter.writerow([p])

		if count >= 0:
			node_list.append([count, p])
			nodewriter.writerow([p])

		count += 1

# EDGE LIST

pprint(topics)
pprint(len(topics))

full_edge_list = []
weighted_edge_list = [["Source", "Target", "Weight"]]

for i in range(0, len(topics)):
	short_list = []

	# For each keyword in a little list
	for j in range(0, 10):
		for k in range(0, len(node_list)):
			if node_list[k][1] == topics[i][j]:
				source_id = node_list[k][0]
				short_list.append(source_id)

	# For the list of keyword ids for an article
	for m in range(0, len(short_list)):

		source_category = short_list[m]
		count = m + 1

		while count < len(short_list):
			full_edge_list.append([source_category, short_list[count], 1])
			count += 1

with open('edges.csv', 'w', newline='') as edge_file:
	edgewriter = csv.writer(edge_file, delimiter=',')
	edgewriter.writerow(["Source", "Target", "Weight"])
	for p in full_edge_list:
		edgewriter.writerow(p)










