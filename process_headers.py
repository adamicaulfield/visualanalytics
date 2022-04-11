import pandas as pd
import csv
import sys

def getEmployeeID(employees, e):
	k = 0
	while(employees[k] != e):
		k = k+1

	return k

# Open senders.txt
employee_file = open("./uqsender.txt", "r")
employees = employee_file.readlines()
for i in range(0, len(employees)):
	employees[i] = employees[i].strip()
# print(senders)
# print(type(senders))

# employees = ['Adam', 'Bob', 'Bill', 'Jack', 'Joe']

# Open CSV
with open("sendrecv.csv") as csvFile:
	reader = csv.reader(csvFile, delimiter=',')
	email_data = [row for row in reader]

email_data = email_data[1:]

# Defining index for the dataframe
# idx = ['1', '2', '3', '4']
idx = employees
  
# Defining columns for the dataframe
# cols = list('ABCD')
cols = employees

send_recv_data = []
for s in employees:
	d = []
	for ss in employees:
		d.append(0)
	send_recv_data.append(d)

# print("First row: "+str(email_data[0]))
print("Scanning data for all messages:")

total = len(email_data)*len(employees)
for i in range(0, len(email_data)):
	
	sender = email_data[i][0]
	sender_id = getEmployeeID(employees, sender)
	count = 0
	# for j in range(0, len(email_data)):
		
	msg = email_data[i][1]
	
	for recv in employees:
		# print("RECV: "+recv)
		if(sender != recv and msg.find(recv) != -1):
			# print(sender+" sent "+email_data[i][2]+" messages to "+recv)
			recv_id = getEmployeeID(employees, recv)
			send_recv_data[sender_id][recv_id] = send_recv_data[sender_id][recv_id] + int(email_data[i][2])
			# print("send_recv_data["+str(sender_id)+"]["+str(recv_id)+"] = "+str(send_recv_data[sender_id][recv_id]))


		count = count + 1
		progress = (100*count)/total
		sys.stdout.write("MSG: %d/%d\t PROGRESS: %d%% \r" % (i, len(email_data), progress) )
		sys.stdout.flush()


# Data for heat map
print("Writing to \'send_recv_data.txt\'")
with open('send_recv_data.txt','w') as my_csv:
	csvWriter = csv.writer(my_csv, delimiter=',')
	csvWriter.writerows(send_recv_data)
print("Done")

source = [] # indices correspond to labels, eg A1, A2, A2, B1, ...
target = []
value = []
total = len(employees)*len(employees)
count = 0
for i in range(0, len(send_recv_data)):
	for j in range(0, len(send_recv_data[0])):
		count = count + 1
		progress = (100*count)/total
		sys.stdout.write("PROGRESS: %d%% \r" % (progress) )
		sys.stdout.flush()
		if i != j and send_recv_data[i][j] > 20:
			source.append(i)
			target.append(j)
			value.append(send_recv_data[i][j])

sankey_data = []
sankey_data.append(source)
sankey_data.append(target)
sankey_data.append(value)

# Data for heat map
print("Writing to \'send_recv_sankey_data.txt\'")
with open('send_recv_sankey_data.txt','w') as my_csv:
	csvWriter = csv.writer(my_csv, delimiter=',')
	csvWriter.writerows(sankey_data)
print("Length of sankey_data: "+str(len(value)))
print("Done")

