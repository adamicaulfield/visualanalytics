import numpy as np
import nltk
from nltk import bigrams
import itertools
import pandas as pd
import sys

# Source:
# https://www.pythonprogramming.in/how-to-calculate-a-word-word-co-occurrence-matrix.html

def generate_co_occurrence_matrix(corpus):
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_index = {word: i for i, word in enumerate(vocab)}
 
    # Create bigrams from all words in corpus
    bi_grams = list(bigrams(corpus))
 
    # Frequency distribution of bigrams ((word1, word2), num_occurrences)
    bigram_freq = nltk.FreqDist(bi_grams).most_common(len(bi_grams))
 
    # Initialise co-occurrence matrix
    # co_occurrence_matrix[current][previous]
    co_occurrence_matrix = np.zeros((len(vocab), len(vocab)))
 
    # Loop through the bigrams taking the current and previous word,
    # and the number of occurrences of the bigram.
    for bigram in bigram_freq:
        current = bigram[0][1]
        previous = bigram[0][0]
        count = bigram[1]
        pos_current = vocab_index[current]
        pos_previous = vocab_index[previous]
        co_occurrence_matrix[pos_current][pos_previous] = count
    co_occurrence_matrix = np.matrix(co_occurrence_matrix)
 
    # return the matrix and the index
    return co_occurrence_matrix, vocab_index

allData = []
punc = '''!()-[]{};:'"\,<>.?@#$%^&*_~'''
# total = 8
articleCount = 844
for a in range(0, articleCount+1):
    filename = "./articles/"+str(a)+".txt"
    progress = 100*a/articleCount
    # print(filename+"\t"+str(a)+"/"+str(articleCount)+"="+str(progress))
    sys.stdout.write("%s %d%% \r" % (filename, progress) )
    sys.stdout.flush()

    with open(filename, "r", errors='replace') as articles_file:
        #articles_file = open(filename, "r")
        articles = articles_file.readlines()


    total = len(articles)
    i = 0
    while i < total:
        articles[i] = articles[i].strip()
        if(len(articles[i])==0):
            articles.remove(articles[i])
            total = total - 1
        else:
            i = i +1

    for i in range(0, len(articles)):
        articles[i] = articles[i].split()

    # Remove Punctuation -- https://www.geeksforgeeks.org/python-remove-punctuation-from-string/

    for i in range(0, len(articles)): # sentence / list
        for j in range(0, len(articles[i])): # word / string
            for elt in articles[i][j]: # character
                if elt in punc:
                    before = articles[i][j]
                    articles[i][j] = articles[i][j].replace(elt, "")
                    #print("Before: "+before+"\tAfter: "+articles[i][j])

        allData.append(articles[i])
print("")

# Create one list using many lists
data = list(itertools.chain.from_iterable(allData))
matrix, vocab_index = generate_co_occurrence_matrix(data)
 
 
df = pd.DataFrame(matrix, index=vocab_index,
                             columns=vocab_index)



# keyFrame = df[key].to_frame()
# keyFrame = keyFrame[(keyFrame.T != 0).any()]
# print(keyFrame.describe())
key = "died"
print(df[key].describe())
keyFrame = df.loc[:,[key]]
print((keyFrame.sort_values(by=key, ascending=False)).head(20))