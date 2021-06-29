import pandas as pd 
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import random, statistics, csv

df = pd.read_csv('sample.csv')
newlist = df['temp'].tolist()

graph = ff.create_distplot([newlist], ['temp'], show_hist = False)
# graph.show()

'''
dist = []
for i in range(0, 100):
    rand = random.randint(0, len(newlist))
    value = newlist[rand]
    dist.append(value)

mean = statistics.mean(dist)
dev = statistics.stdev(dist)
'''

dist = []
for i in range(0, 2500):
    rand = random.randint(0, len(newlist))
    value = newlist[rand]
    dist.append(value)

mean = statistics.mean(dist)
dev = statistics.stdev(dist)

graph = ff.create_distplot([dist], ['temp'], show_hist = False)
graph.show()