# Python program to generate a heatmap  
# which represents panda dataframe
# in colour coding schemes
  
# import required libraries
import matplotlib.pyplot as plt
import pandas as pd
import csv
import plotly.graph_objects as go
import numpy as np

with open("send_recv_data.txt") as csvFile:
	reader = csv.reader(csvFile, delimiter=',')
	send_recv_data = [row for row in reader]

for i in range(0, len(send_recv_data)):
	for j in range(0, len(send_recv_data[0])):
		send_recv_data[i][j] = int(send_recv_data[i][j])

employee_file = open("./uqsender.txt", "r")
employees = employee_file.readlines()
for i in range(0, len(employees)):
	employees[i] = employees[i].strip()
	employees[i] = employees[i] + " ("+str(i)+")"

# Entering values in the index and columns  
# and converting them into a panda dataframe
df = pd.DataFrame(send_recv_data)
# df = pd.DataFrame([[10, 20, 30, 40], [50, 30, 8, 15],
                   # [25, 14, 41, 8], [7, 14, 21, 28]],
                   # columns = cols, index = idx)

plt.figure(dpi=300)
plt.rc('font', size=4)

# Displaying dataframe as an heatmap
# with diverging colourmap as RdYlBu
plt.imshow(df, cmap ="jet")
  
# Displaying a color bar to understand
# which color represents which range of data
plt.colorbar()

# Assigning labels of x-axis 
# according to dataframe
plt.xticks(range(len(df)), df.columns, rotation=15, ha="left")
  
# Assigning labels of y-axis 
# according to dataframe
plt.yticks(range(len(df)), df.index)

plt.xlabel("Recipient IDs")
plt.ylabel("Sender IDs")

plt.title("Frequency of sent and received emails")
# Displaying the figure
# plt.show()
plt.savefig("emails.png")


fig = go.Figure(data=go.Heatmap(
        z=send_recv_data,
        x=employees,
        y=employees,
        colorscale='jet'))

fig.update_xaxes(side="top")
fig.update_layout(
    autosize=True,
    xaxis_nticks=55,
    yaxis_nticks=55)
# fig.show()
fig.write_html("./heatmap.html")