__author__ = 'yi-linghwong'

import os
import sys
import random


#################
# ENTER THE TOPIC NUMBER HERE
#################

topic_number = 4

##################


lines1 = open('/Users/yi-linghwong/GitHub/_big_files/mallet/composition_file/streaming_space_composition.txt','r').readlines()
lines2 = open('/Users/yi-linghwong/GitHub/_big_files/twitter/raw_streaming_space.csv','r').readlines()

tweet_index_list = []
count = 0

print ("Getting index for topic...")

for line in lines1[1:]:

    spline = line.rstrip('\n').split('\t')

    for n in range(2,22,2):

        if int(spline[n]) == topic_number:

            if float(spline[n+1]) > 0.9:
                tweet_index_list.append(int(spline[0]))
                #count += 1

print (len(tweet_index_list))

index_list_random = random.sample(tweet_index_list, 100)

#print (index_list_random)

print ()

print ("Getting tweets...")
print ()

tweets = []

for index,line in enumerate(lines2):

    spline = line.rstrip('\n').split(',')

    if index in index_list_random:

        print (spline[0],spline[1],spline[-1])

        #tweets.append([spline[0],spline[1],spline[-1]])



