# import required libraries
import matplotlib.pyplot as plt
import pandas as pd
import csv
import plotly.graph_objects as go

with open("send_recv_sankey_data.txt") as csvFile:
	reader = csv.reader(csvFile, delimiter=',')
	sankey_data = [row for row in reader]

for i in range(0, len(sankey_data)):
	for j in range(0, len(sankey_data[0])):
		sankey_data[i][j] = int(sankey_data[i][j])

employee_file = open("./uqsender.txt", "r")
employees = employee_file.readlines()
for i in range(0, len(employees)):
	employees[i] = employees[i].strip()
	employees[i] = employees[i] + " ("+str(i)+")"


fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 1),
      label = employees,
      #hovertemplate='Node %{label} has total value %{value}<extra></extra>',
      color = "blue"
    ),
    link = dict(
      source = sankey_data[0], #[0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = sankey_data[1], #2, 3, 3, 4, 4, 5],
      value = sankey_data[2], #[8, 4, 2, 8, 4, 2],
      hovertemplate='Messages from %{source.label}<br />'+
        'to %{target.label}: %{value}'+
        '<br /><extra></extra>',
  ))])

fig.update_layout(
	# title_text="Sender-Recipient pairs with more than 20 email messages exchanged",
	autosize=True,
	font=dict(size = 18, color = 'black')
	)
# fig.show()
fig.write_html("./sankey.html")