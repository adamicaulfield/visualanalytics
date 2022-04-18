import numpy as np
import matplotlib.pyplot as plt
import csv
import json
from math import pi

print("---------------- Article Sentiment ----------------")
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

labels = range(0, totalArticles)

with open('articles_dictionary.txt') as f:
    data = f.read()
allArticles = json.loads(data)

'''
for art in allArticles.keys():
	print(art)
	for key in allArticles[art].keys():
		print(key+"\t"+str(allArticles[art][key]))
	print(" ")
'''

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


#plt.scatter(labels, pos, label="pos", color="red", marker=".")
#plt.scatter(labels, neg, label="neg", c="blue", marker=".")

#plt.legend()
#plt.show()

print(" ")
print("---------------- Publisher Sentiment ----------------")
with open("publisher_sentiment.txt") as csvFile:
	reader = csv.reader(csvFile, delimiter=',')
	publisherSentiments = [row for row in reader]

labels = publisherSentiments[4]
publisherSentiments = publisherSentiments[:4]
for i in range(0, len(publisherSentiments)):
	for j in range(0, len(publisherSentiments[0])):
		publisherSentiments[i][j] = float(publisherSentiments[i][j])
		

pos = publisherSentiments[0]
neg = publisherSentiments[1]
neu = publisherSentiments[2]
count = publisherSentiments[3]
print("\tpos\tneg\tneu\tcount")
print("mean\t{0}\t{1}\t{2}\t{3}".format(
		round(np.mean(pos),4),
		round(np.mean(neg),4),
		round(np.mean(neu),4),
		round(np.mean(count),4),
))
print("std\t{0}\t{1}\t{2}\t{3}".format(
		round(np.std(pos),4),
		round(np.std(neg),4),
		round(np.std(neu),4),
		round(np.std(count),4)
))
print("min\t{0}\t{1}\t{2}\t{3}".format(np.min(pos),np.min(neg),np.min(neu),np.min(count)))
print("1Q\t{0}\t{1}\t{2}\t{3}".format(
	np.percentile(pos, 25),
	np.percentile(neg, 25),
	np.percentile(neu, 25),
	np.percentile(count, 25)
))
print("median\t{0}\t{1}\t{2}\t{3}".format(
	np.median(pos),
	np.median(neg),
	np.median(neu),
	np.median(count)
))
print("3Q\t{0}\t{1}\t{2}\t{3}".format(
	np.percentile(pos, 75),
	np.percentile(neg, 75),
	np.percentile(neu, 75),
	np.percentile(count, 75)
))
print("max\t{0}\t{1}\t{2}\t{3}".format(
	np.max(pos),
	np.max(neg),
	np.max(neu),
	np.max(count)
))

fig, ax = plt.subplots()
ax.scatter(neg, pos, s=count, color="black", marker=".")

#a=np.std(neg)       #radius on the x-axis
#b=np.std(pos)	    #radius on the y-axis
#ax.plot( u+a*np.cos(t) , v+b*np.sin(t) , color="red", alpha=0.3)

#a=3*np.std(neg)       #radius on the x-axis
#b=3*np.std(pos)       #radius on the y-axis
#ax.plot( u+a*np.cos(t) , v+b*np.sin(t) , color="red", alpha=0.9)
plt.xlim([0,1])
plt.ylim([0,1])
plt.xlabel("Negative Proportion")
plt.ylabel("Positive Proportion")



print(" ")
sig_pos = []
sig_neg = []
sig_count = [[],[],[]]
std_thresh = 2
u=0.5     			#x-position of the center
v=0.5			    #y-position of the center
a=std_thresh*np.std(neg)       #radius on the x-axis
b=std_thresh*np.std(pos)       #radius on the y-axis
t = np.linspace(0, 2*pi, 100)
#ax.plot( u+a*np.cos(t) , v+b*np.sin(t) , color="red", alpha=0.6, label=str(std_thresh)+" Std Devs from Mean")
plt.axvline(x=np.mean(neg)+std_thresh*np.std(neg),color="red", alpha=0.6, label=str(std_thresh)+" Std Devs (Neg)")
plt.axvline(x=np.mean(neg)-std_thresh*np.std(neg),color="red", alpha=0.6)

plt.axhline(y=np.mean(pos)+std_thresh*np.std(pos),color="green", alpha=0.6, label=str(std_thresh)+" Std Devs (Pos)")
plt.axhline(y=np.mean(pos)-std_thresh*np.std(pos),color="green", alpha=0.6)
for i in range(0, len(labels)):
	q1 =  (pos[i] >= std_thresh*np.std(pos)+np.mean(pos))
	q2 =  (pos[i] <= -1*std_thresh*np.std(pos)+np.mean(pos))
	q3 =  (neg[i] >= std_thresh*np.std(neg)+np.mean(neg))
	q4 =  (neg[i] <= -1*std_thresh*np.std(neg)+np.mean(neg))
	
	ann = (q1 or q2 or q3 or q4)

	if ann:
		if q1 or q2:	
			print("Significant pos: "+labels[i]+" pos:"+str(pos[i]))
		if q3 or q4:
			print("Significant neg: "+labels[i]+" neg:"+str(neg[i]))

		sig_neg.append(neg[i])
		sig_pos.append(pos[i])

		ax.annotate(labels[i], (neg[i], pos[i]))

	'''
	p1 = (count[i] >= std_thresh*np.std(count)+np.mean(count))
	p2 = (count[i] <= -1*std_thresh*np.std(count)+np.mean(count))

	if p1 or p2:
		print("Significant count: "+labels[i])
		sig_count[0].append(neg[i])
		sig_count[1].append(pos[i])
		sig_count[2].append(count[i])
		ax.annotate(labels[i], (neg[i], pos[i]))
	'''

plt.scatter(sig_neg, sig_pos, color="blue", marker="*", label="Significant pos or neg sentiment")
#plt.scatter(sig_count[0], sig_count[1], s=sig_count[2], color="green", marker=".", label="Significant count")

plt.legend(loc=1)
plt.show()

fig, axs = plt.subplots(2, 2)
axs[0,0].boxplot(pos)
axs[0,0].set_title('Positive')
axs[0,1].boxplot(neg)
axs[0,1].set_title('Negative')
axs[1,0].boxplot(neu)
axs[1,0].set_title('Neutral')
axs[1,1].boxplot(count)
axs[1,1].set_title('Total Articles')
plt.show()

for publisher in labels:
	print(publisher)
	for key in allArticles.keys():
		if allArticles[key]['publisher'] == publisher:
			print(key+"\t"+allArticles[key]['date']+"\t"+str(allArticles[key]['sentiment']))
	print(" ")