__author__ = 'yi-linghwong'

##################
# create one single input file for Gephi (one instance per line)
##################

import os
import sys

#lines = open('../mallet_input/preprocessed_files/facebook/preprocessed_fb_comments_20160121_en.csv','r').readlines()
lines = open('../../_big_files/facebook/preprocessed_fb_comments_replies_20160223_en.csv','r').readlines()

messages = []

# get number of elements per line for checking

for line in lines[:1]:
    spline = line.replace('\n','').split(',')
    length = len(spline)

print ("Number of elements per line is "+str(length))

print (len(lines))

# get first (username) and last (message) element of the line

for line in lines:
    spline = line.replace('\n','').split(',')

    if (len(spline)) == length:

        # remove leading whitespace from message
        spline[-1] = spline[-1].lstrip()

        messages.append([spline[0],'en',spline[-1]])

    else:
        print ("error")
        print (spline)

print (len(messages))

# write output to file

#f = open('../mallet_input/single_file/facebook/fb_comments_20160121_en.txt','w')
f = open('../../_big_files/mallet/input/fb_comments_replies_20160223_en.txt','w')

for m in messages:
    f.write(' '.join(m)+'\n')

f.close()