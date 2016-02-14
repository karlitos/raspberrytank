#!/usr/bin/python
import matplotlib.pyplot as plt
import pandas as pd

# Read data and count occurencies
csv_data = pd.read_csv('./captures/idle binary.csv')

occurencies = csv_data['Data'].value_counts().reset_index()
occurencies.columns = ['bits', 'count']
occurencies['stripped bits'] = occurencies['bits'].str.replace('(0b| )', '')

print occurencies[['stripped bits', 'count']].values.tolist()

# prepare table data
columns = ('stripped bits', 'count')
rows = ['%s.' % (x + 1) for x in occurencies.index]
cells = occurencies[['stripped bits', 'count']].values.tolist()

# set figure size
# nrows, ncols = len(cells)+1, len(columns)
# hcell, wcell = 0.3, 1.
# hpad, wpad = 0, 0
# fig=plt.figure(figsize=(ncols*wcell+wpad, nrows*hcell+hpad))

#
ax = plt.gca() # get current axis
ax.axis('off')

# Plot a table
the_table = ax.table(cellText=cells,
                      rowLabels=rows,
                      #rowColours=colors,
                      colLabels=columns,
                      cellLoc='center',
                      loc='center')

#the_table.auto_set_font_size(False)
#the_table.set_fontsize(14)
the_table.scale(1, 2)
plt.title('Idle - binary code')
#plt.show()
plt.savefig("table.png")
