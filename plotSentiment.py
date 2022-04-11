import numpy as np
import matplotlib.pyplot as plt
import csv

with open("articles_sentiment.txt") as csvFile:
	reader = csv.reader(csvFile, delimiter=',')
	allSentiment = [row for row in reader]

for i in range(0, len(allSentiment)):
	for j in range(0, len(allSentiment[0])):
		allSentiment[i][j] = float(allSentiment[i][j])
		
pos = allSentiment[0]
neg = allSentiment[1]
neu = allSentiment[2]
totalArticles = len(pos)

#Scatter plots
labels = range(0, totalArticles)
#fig,axes = plt.subplots(nrows=2)

#axes[0].scatter(labels, pos, label="pos", color="red", marker=".")
#axes[1].scatter(labels, neg, label="neg", c="blue", marker=".")

#axes[0].legend()
#axes[1].legend()

plt.scatter(labels, pos, label="pos", color="red", marker=".")
plt.scatter(labels, neg, label="neg", c="blue", marker=".")

plt.legend()
plt.show()

"""
# Stacked bar charts
plt.rcParams.update({'font.size': 12})

fig,axes = plt.subplots(nrows=13)
fig.subplots_adjust(hspace=0.5, wspace=0.3)

labels = range(0, totalArticles)
print(len(labels))
print(len(pos))
plotItems = 65
for i,ax in enumerate(axes.flat):
	
	start = i*plotItems
	end = (i+1)*plotItems

	#ax.bar(labels, neu, width=0.3, yerr=np.std(neu), label='neu')
	#ax.bar(labels, pos, width=0.3, yerr=np.std(pos), label='pos',bottom=neu)
	#ax.bar(labels, neg, width=0.3, yerr=np.std(neg), label='neg', bottom=np.add(pos,neu))

	ax.bar(labels[start:end], neg[start:end], label='neg')
	ax.bar(labels[start:end], pos[start:end], label='pos',bottom=neg[start:end])
plt.legend()
plt.show()
"""