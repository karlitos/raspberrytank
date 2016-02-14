#!/usr/bin/python
import matplotlib.pyplot as plt
import pandas as pd

# data = {}
#
# with open('./captures/idle.csv', 'rb') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#
#     for row in reader:
#         # initialize the array if necessary
#         data[row[0]] =  data.get(row[0],[])
#         if 'binary' in row[1]:
#             print row[2][2:].replace(" ", "")
#         # insert the data
#         data[row[0]].append(row[2])


csv_data = pd.read_csv('./captures/idle binary.csv')

occurencies = csv_data['Data'].value_counts().reset_index()
occurencies.columns = ['bits', 'count']
occurencies['stripped bits'] = occurencies['bits'].str.replace('(0b| )', '')

print occurencies[['stripped bits', 'count']]
