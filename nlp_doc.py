import nltk
import numpy as np
import matplotlib.pyplot as plt
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

print("Sentiment Analysis:")

totalArticles = 844
allData = []
pos = []
neg = []
neu = []

allPublishers = {}
for a in range(0, totalArticles+1):
	filename = "../MC1Data/MC1Data/articles/"+str(a)+".txt"

	with open(filename, "r", errors='replace') as articles_file:
		#articles_file = open(filename, "r")
		articles = articles_file.readlines()
		#articles = articles_file.read()

	total = len(articles)
	i = 0
	while i < total:
		articles[i] = articles[i].strip()
		if(len(articles[i])==0):
		    articles.remove(articles[i])
		    total = total - 1
		else:
		    i = i +1

	publisher = articles[0]
	title = articles[1]
	date = articles[2]

	art_sentiment = {'pos':0, 'neg':0, 'neu':0}
	

	for sentence in articles[3:]:
		sid = SentimentIntensityAnalyzer()
		#print("Sentence: "+sentence)
		ss = sid.polarity_scores(sentence)
		#print("ss: :"+str(ss))
		#print(" ")
		for key in art_sentiment.keys():
			art_sentiment[key] = round(art_sentiment[key] + ss[key]/len(articles[3:]), 4)
	
	print(str(a)+".txt \t"+str(art_sentiment))
	allData.append(art_sentiment)
	pos.append(art_sentiment['pos'])
	neg.append(art_sentiment['neg'])
	neu.append(art_sentiment['neu'])

	if publisher not in allPublishers.keys():
		allPublishers[publisher] = art_sentiment
		allPublishers[publisher]["count"] = 1
	else:
		for key in art_sentiment.keys():
			allPublishers[publisher][key] = allPublishers[publisher][key] + art_sentiment[key]
			allPublishers[publisher]["count"] = allPublishers[publisher]["count"]+1

print(" ")
print("\tpos\tneg\tneu")
print("mean\t{0}\t{1}\t{2}".format(
		round(np.mean(pos),4),
		round(np.mean(neg),4),
		round(np.mean(neu),4)
))
print("std\t{0}\t{1}\t{2}".format(
		round(np.std(pos),4),
		round(np.std(neg),4),
		round(np.std(neu),4)
))
print("min\t{0}\t{1}\t{2}".format(np.min(pos),np.min(neg),np.min(neu)))
print("1Q\t{0}\t{1}\t{2}".format(np.percentile(pos, 25),np.percentile(neg, 25),np.percentile(neu, 25)))
print("median\t{0}\t{1}\t{2}".format(np.median(pos),np.median(neg),np.median(neu)))
print("3Q\t{0}\t{1}\t{2}".format(np.percentile(pos, 75),np.percentile(neg, 75),np.percentile(neu, 75)))
print("max\t{0}\t{1}\t{2}".format(np.max(pos),np.max(neg),np.max(neu)))

# Output Data
allSentiment = [pos, neg, neu]
print("Writing to \'articles_sentiment.txt\'")
with open('articles_sentiment.txt','w') as my_csv:
	csvWriter = csv.writer(my_csv, delimiter=',')
	csvWriter.writerows(allSentiment)
print("Length: "+str(len(allSentiment)))
print("Done")
print(" ")

for publisher in allPublishers.keys():
	print(publisher)
	print(allPublishers[publisher])
