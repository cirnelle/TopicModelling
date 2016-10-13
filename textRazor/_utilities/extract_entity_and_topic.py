__author__ = 'yi-linghwong'

import os
import sys
import re
import textrazor
import random

class ExtractEntities():

    def __init__(self):

        # set api key

            api_file = open('../../../../keys/textrazor_api_key.txt','r').readlines()

            api_key = api_file[0]

            textrazor.api_key = api_key

    def create_input_file(self):

        lines = open(path_to_raw_messages,'r').readlines()

        print (len(lines))

        raw_messages = []

        for line in lines:

            spline = line.rstrip('\n').split(',')
            spline[-1] = re.sub(r'(?:https?\://)\S+', ' ', spline[-1]) #remove URLs
            raw_messages.append(spline[-1])

        random_sample = random.sample(raw_messages, 2300)

        print (len(random_sample))

        messages = ' '.join(random_sample)

        return (messages)


    def extract_entities_and_topic(self):

        messages = self.create_input_file()

        client = textrazor.TextRazor(extractors=["entities", "topics"])

        client.set_classifiers(["textrazor_newscodes"])

        response = client.analyze(messages)

        #---------------------
        # extract entities

        entities = list(response.entities())
        entities.sort(key=lambda x: x.relevance_score, reverse=True) #sort to show most relevant entities first

        seen = set()
        entities_list = []

        for e in entities:

            if e.id not in seen and len(seen) < 20:
                print (e.id, e.relevance_score, e.confidence_score, e.freebase_types)
                #print(e.id, e.matched_text, e.matched_words)
                entities_list.append([str(e.id), str(e.relevance_score), str(e.confidence_score), str(e.wikipedia_link), str(e.freebase_types)])
                seen.add(e.id)

        #-----------------------
        # extract topics


        topics = response.topics()
        topics.sort(key=lambda x: x.score, reverse=True)  # sort to show most relevant topics first

        topic_list = []

        for t in response.topics():
            if t.score > 0.5 and len(topic_list) < 100:
                #print (t.label, t.score)
                topic_list.append([str(t.label), str(t.score)])


        #------------------------
        # write to file


        f = open(path_to_store_entities,'w')

        for el in entities_list:

            f.write('\t'.join(el)+'\n')

        f.close()


        f = open(path_to_store_topics, 'w')

        for t in topic_list:
            f.write(','.join(t)+'\n')

        f.close()




################
# variables
################
path_to_raw_messages = '/Users/yi-linghwong/GitHub/_big_files/twitter/raw_streaming_space.csv'
path_to_store_entities = '../output/entities_space.csv'
path_to_store_topics = '../output/topics_space.csv'

if __name__ == '__main__':

    ee = ExtractEntities()

    #ee.create_input_file()
    ee.extract_entities_and_topic()