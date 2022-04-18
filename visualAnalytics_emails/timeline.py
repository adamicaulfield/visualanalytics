import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
#
# xy_val= [{'date': '2014-01-13', 'time': '16:48', 'value': 'FW: ARISE  Mies Haber'},
#          {'date': '2014-01-13', 'time': '19:28', 'value': 'FW: ARISE Loreto Bodrogi'},
#          {'date': '2014-01-13', 'time': '19:31', 'value': 'FW: ARISE Inga Ferro'},
#          {'date': '2014-01-13', 'time': '20:05', 'value': 'FW: ARISE Isia vann'},
#          {'date': '2014-01-13', 'time': '21:33', 'value': 'FW: ARISE Ferro'}]
#
# list_of_hours = []
# for i in range(0, len(xy_val)):
#     list_of_hours.append(xy_val[i]["time"])
#
# list_of_values= []
# for i in range(0, len(xy_val)):
#     list_of_values.append(xy_val[i]["value"])
#
#
# plt.plot(list_of_hours, list_of_values, label='Consumo')
# plt.show()
#
# In case the above fails, e.g. because of missing internet connection
# use the following lists as fallback.
names = ['Man your battles tations from Baza  ',
         'Re:Man your battles tations from Flecha',
         'Re: Man your battles tations from Flecha',
         'Man your battles tations from Baza',
         'Man your battles tations from Calixto',
         'Man your battles tations from Calixto',
         'Man your battles tations from Baza']

dates = ['11:21',
         '11:25',
         '12:05',
         '12:48',
         '13:01',
         '13:12',
         '13:27']

# Convert date strings (e.g. 2014-10-18) to datetime
dates = [datetime.strptime(d,"%H:%M") for d in dates]

# Choose some nice levels
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title="Matplotlib release dates")

ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")

# format xaxis with 4 month intervals
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()