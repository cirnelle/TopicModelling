__author__ = 'yi-linghwong'

import sys
import os
import networkx as nx

class CreateGraph():

    def create_topic_composition_graph(self):

        G = nx.Graph()

        lines = open(path_to_topic_composition_file,'r').readlines()
        #lines = open('test.txt','r').readlines()

        ###################
        # Create edges list
        ###################

        edges = []

        number_of_topics = 10
        n = number_of_topics + 1

        for line in lines:
            spline = line.replace('\n','').split('\t')

            for x in range(1,n):

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

        for x in range(number_of_topics):
            nodes.append('Topic_'+str(x))

        print ("Number of nodes is "+str(len(nodes)))


        G.add_edges_from(edges)
        G.add_nodes_from(nodes)

        nx.write_gexf(G, path_to_store_topic_composition_graph)


    def create_topic_keywords_graph(self):

        G = nx.Graph()

        lines = open(path_to_topic_keywords_file,'r').readlines()

        ##################
        # create edge list
        ##################

        edges = []
        number_of_keywords = 19
        n = number_of_keywords + 2


        for line in lines:
            spline = line.replace('\n','').split('\t')

            for x in range(2,n):
                topic = 'Topic_'+str(spline[0])
                keyword = spline[x]

                edges.append([topic,keyword])

        print ("Number of edges is "+str(len(edges)))

        ##################
        # create node list
        ##################

        nodes = []
        keywords = []

        for line in lines:
            spline = line.replace('\n','').split('\t')
            topic = 'Topic_'+str(spline[0])

            nodes.append(topic)

            for x in range(2,n):
                if spline[x] not in keywords:
                    keywords.append(spline[x])

                    nodes.append(spline[x])

                else:
                    print ("Duplicated keyword "+str(spline[x]))

        print ("Number of nodes is "+str(len(nodes)))

        G.add_edges_from(edges)
        G.add_nodes_from(nodes)

        nx.write_gexf(G, path_to_store_topic_keywords_graph)


###############
# variables
###############

path_to_topic_composition_file = '../output/models/space_tweets_composition.txt'
path_to_store_topic_composition_graph = "../GEPHI/graph_files/space_tweets_composition_raw.gexf"
path_to_topic_keywords_file = '../output/models/space_tweets_keys.txt'
path_to_store_topic_keywords_graph = '../GEPHI/graph_files/space_tweets_keys_raw.gexf'


if __name__ == '__main__':

    cg = CreateGraph()

    cg.create_topic_composition_graph()
    #cg.create_topic_keywords_graph()




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