__author__ = 'yi-linghwong'

import sys
import os
import networkx as nx

G = nx.Graph()

lines = open('../output/models/space_tweets_composition.txt','r').readlines()
#lines = open('test.txt','r').readlines()

###################
# Create edges list
###################

edges = []

for line in lines:
    spline = line.replace('\n','').split('\t')

    for x in range(1,11):

        user = spline[1]
        topic = 'Topic_'+str(spline[2*x])
        weight = round((float(spline[(2*x)+1]) * 100),2)

        edges.append([user,topic,{'weight':weight}])

print ("Number of edges is "+str(len(edges)))

##################
# Create node list
##################

nodes = []

# create nodes for each user

for line in lines:
    spline = line.replace('\n','').split('\t')

    nodes.append(spline[1])

# create nodes for each topic

for x in range(10):
    nodes.append('Topic_'+str(x))

print ("Number of nodes is "+str(len(nodes)))


G.add_edges_from(edges)
G.add_nodes_from(nodes)

nx.write_gexf(G, "../GEPHI/graph_files/space_tweets_raw.gexf")


'''
G = nx.Graph()

#G.add_nodes_from([(3, {'time':'2pm'}),(4,{'time':'4pm'})])

G.add_nodes_from(['john','jane','peter','simone','ling'], time='2pm')
G.node['john']['room'] = 714
#G.add_node(1)

print (G.nodes(data=True))

G.add_edge('john', 'jane', weight=4.7)
#G.add_edges_from([['john','jane',{'color':'blue'}], ['jane','peter',{'weight':8}]])
G.add_edges_from([['john','jane', {'weight':4.3}], ['jane','peter', {'weight':8.2}]])
G.edge['jane']['peter']['color'] = 'red'

print (G.edges(data=True))

nx.write_gexf(G, "test.gexf")

'''