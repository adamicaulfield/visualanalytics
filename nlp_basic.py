import numpy as np
import pandas as pd
import sys
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

#Source
#https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk

allData = []
punc = '''!()-[]{};:'"\,<>.?@#$%^&*_~'''
articleCount = 844



a = 0
filename = "../MC1Data/MC1Data/articles/"+str(a)+".txt"

with open(filename, "r", errors='replace') as articles_file:
    #articles_file = open(filename, "r")
	#articles = articles_file.readlines()
    articles = articles_file.read()

stop_words=set(stopwords.words("english"))
sentences = sent_tokenize(articles)
sent_tokens = []
for w in sentences:
	if w not in stop_words:
		sent_tokens.append(w)

word_tokens = word_tokenize(articles)

# Training data from Kaggle https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data?select=train.tsv.zip
data=pd.read_csv('train.tsv', sep='\t')
data.info()
# 0 - negative, 1 - somewhat negative, 2 - neutral, 3 - somewhat positive, 4 - positive
print(data.Sentiment.value_counts())
Sentiment_count=data.groupby('Sentiment').count()
plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])
plt.xlabel('Review Sentiments')
plt.ylabel('Number of Review')
plt.show()

#Bag of Words model
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(lowercase=True,stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
text_counts= cv.fit_transform(data['Phrase'])

#Split train and test sets
X_train, X_test, y_train, y_test = train_test_split(text_counts, data['Sentiment'], test_size=0.3, random_state=1)

# Model Building and Evaluation
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print("MultinomialNB Accuracy (BoW):",metrics.accuracy_score(y_test, predicted))

# Feature Generation using TF-IDF
tf=TfidfVectorizer()
text_tf= tf.fit_transform(data['Phrase'])

#Split train and test sets
X_train, X_test, y_train, y_test = train_test_split(text_tf, data['Sentiment'], test_size=0.3, random_state=123)

# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print("MultinomialNB Accuracy (TF-IDF):",metrics.accuracy_score(y_test, predicted))
