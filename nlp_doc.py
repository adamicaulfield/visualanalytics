import nltk
import numpy as np
import matplotlib.pyplot as plt
import csv
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer

print("Sentiment Analysis:")
totalArticles = 844
allData = []
pos = []
neg = []
neu = []
print("------------------------ Sentiment of Publishers ------------------------")
allPublishers = {}
allArticles = {}
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
	allArticles[a] = {}
	allArticles[a]['publisher'] = articles[0]
	allArticles[a]['title'] = articles[1]
	allArticles[a]['date'] = articles[2]
	
	art_sentiment = {'pos':0, 'neg':0, 'neu':0, 'compound':0}
	
	for sentence in articles[3:]:
		sid = SentimentIntensityAnalyzer()
		#print("Sentence: "+sentence)
		ss = sid.polarity_scores(sentence)
		#print("ss: :"+str(ss))
		#print(" ")
		for key in art_sentiment.keys():
			art_sentiment[key] = round(art_sentiment[key] + ss[key]/len(articles[3:]), 4)
	
	print(str(a)+".txt\t"+str(ss))
	allData.append(art_sentiment)
	pos.append(art_sentiment['pos'])
	neg.append(art_sentiment['neg'])
	neu.append(art_sentiment['neu'])

	allArticles[a]['sentiment'] = art_sentiment
	
	publisher = articles[0]
	if publisher not in allPublishers.keys():
		allPublishers[publisher] = {'pos':0, 'neg':0, 'neu':0, 'count':0}
	
	if art_sentiment['compound'] > 0:
		allPublishers[publisher]['pos'] = allPublishers[publisher]['pos']+1
	else:
		if art_sentiment['compound'] < 0:
			allPublishers[publisher]['neg'] = allPublishers[publisher]['neg']+1
		else:
			allPublishers[publisher]['neu'] = allPublishers[publisher]['neu']+1
	allPublishers[publisher]["count"] = allPublishers[publisher]["count"]+1

# Output Data
allSentiment = [pos, neg, neu]
print("Writing to \'articles_sentiment.txt\'")
with open('articles_sentiment.txt','w') as my_csv:
	csvWriter = csv.writer(my_csv, delimiter=',')
	csvWriter.writerows(allSentiment)
print("Done")
print(" ")

print("Writing to \'articles_dictionary.txt\'")
with open('articles_dictionary.txt','w') as sentimentDictFile:
	json.dump(allArticles, sentimentDictFile)
print("Done")
print(" ")

print("------------------------ Sentiment of Publishers ------------------------")
# publisherSentiments = [pos, neg, neu, count, publisher]
publisherSentiments = [[],[],[],[],[]]
for publisher in allPublishers.keys():
	i = 0
	for key in allPublishers[publisher].keys():
		if key != 'count':
			allPublishers[publisher][key] = round(allPublishers[publisher][key]/allPublishers[publisher]['count'],4)
		
		publisherSentiments[i].append(allPublishers[publisher][key])		
		i = i+1	
	print(publisher+"\t"+str(allPublishers[publisher]))
	publisherSentiments[4].append(publisher)

print("Writing to \'publisher_sentiment.txt\'")
with open('publisher_sentiment.txt','w') as my_csv:
	csvWriter = csv.writer(my_csv, delimiter=',')
	csvWriter.writerows(publisherSentiments)
print(" ")





