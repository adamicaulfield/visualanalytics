import nltk
import numpy as np
import matplotlib.pyplot as plt
import csv
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
<<<<<<< HEAD
from nltk.tokenize import word_tokenize
from nltk.collocations import *

=======
from nltk.collocations import *
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
>>>>>>> 0fe7d88dfa02bc1ad2a5ef3436d7df791f4a530b

# # Use once if packages have never been installed
# print("Downloading \'vader_lexicon\'")
# nltk.downloader.download('vader_lexicon')
# print("Done downloading \'vader_lexicon\'")
# nltk.download('punkt')
# print("Done downloading \'punkt\'")
# nltk.download('stopwords')
# print("Done downloading \'stopwords\'")
# print(" ")

print("Sentiment Analysis:")
totalArticles = 844
allData = []
pos = []
neg = []
neu = []
print("------------------------ Sentiment of Articles ------------------------")
allPublishers = {}
allArticles = {}
allFilteredWords = []
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
	
<<<<<<< HEAD
	all_words = []
=======
	words = []
	tokenizer = nltk.RegexpTokenizer(r"\w+")
>>>>>>> 0fe7d88dfa02bc1ad2a5ef3436d7df791f4a530b
	for sentence in articles[3:]:
		words = []
		words.append(word_tokenize(sentence))		

		sid = SentimentIntensityAnalyzer()
		#print("Sentence: "+sentence)
		ss = sid.polarity_scores(sentence)
		#print("ss: :"+str(ss))
		#print(" ")
		for key in art_sentiment.keys():
			art_sentiment[key] = round(art_sentiment[key] + ss[key]/len(articles[3:]), 4)
		
		words = words + tokenizer.tokenize(sentence)

	filtered_words = [word for word in words if word not in stopwords.words('english')]

	print(str(a)+".txt\t"+str(ss))
	allData.append(art_sentiment)
	pos.append(art_sentiment['pos'])
	neg.append(art_sentiment['neg'])
	neu.append(art_sentiment['neu'])

	allArticles[a]['sentiment'] = art_sentiment
	
	publisher = articles[0]
	if publisher not in allPublishers.keys():
		allPublishers[publisher] = {'pos':0, 'neg':0, 'neu':0, 'count':0}
	
	if art_sentiment['compound'] >= 0.05:
		allPublishers[publisher]['pos'] = allPublishers[publisher]['pos']+1
	else:
		if art_sentiment['compound'] <= -0.05:
			allPublishers[publisher]['neg'] = allPublishers[publisher]['neg']+1
		else:
			allPublishers[publisher]['neu'] = allPublishers[publisher]['neu']+1
	allPublishers[publisher]["count"] = allPublishers[publisher]["count"]+1

<<<<<<< HEAD
'''
# Uncomment for most common words
	for sentence in words:
		bigram_measures = nltk.collocations.BigramAssocMeasures()
		trigram_measures = nltk.collocations.TrigramAssocMeasures()
		fourgram_measures = nltk.collocations.QuadgramAssocMeasures()
		finder = BigramCollocationFinder.from_words(sentence)
		print(finder.nbest(bigram_measures.pmi, 10))
'''
=======
	allFilteredWords = allFilteredWords + filtered_words

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
fourgram_measures = nltk.collocations.QuadgramAssocMeasures()
finder = BigramCollocationFinder.from_words(allFilteredWords)
ignored_words = nltk.corpus.stopwords.words('english')
finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
print(" ")
print("------------------------ Most common collocations ------------------------")
best = finder.nbest(bigram_measures.raw_freq, 20)
for item in best:
	print(item)
print(" ")
>>>>>>> 0fe7d88dfa02bc1ad2a5ef3436d7df791f4a530b

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