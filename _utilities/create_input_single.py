__author__ = 'yi-linghwong'

##################
# create one single input file for Gephi (one instance per line)
##################

import os
import sys

lines = open('../input/preprocessed_tweets/preprocessed_mars_and_water_stream.csv','r').readlines()

tweets = []

# get number of elements per line for checking

for line in lines[:1]:
    spline = line.replace('\n','').split(',')
    length = len(spline)

print ("Number of elements per line is "+str(length))

print (len(lines))

# get first (username) and last (tweet) element of the line

for line in lines:
    spline = line.replace('\n','').split(',')

    if (len(spline)) == length:

        tweets.append([spline[0],spline[-1]])

    else:
        print ("error")
        print (spline)

print (len(tweets))

# write output to file

f = open('../input/single_file_tweets/mars_and_water_stream.txt','w')

for t in tweets:
    f.write(' '.join(t)+'\n')

f.close()