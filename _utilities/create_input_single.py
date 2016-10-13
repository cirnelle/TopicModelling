__author__ = 'yi-linghwong'

##################
# create one single input file for Gephi (one instance per line)
##################

import os
import sys
import time

#lines = open('../mallet_input/preprocessed_files/facebook/preprocessed_fb_comments_20160121_en.csv','r').readlines()
lines = open('../../_big_files/twitter/preprocessed_#streaming_space.csv','r').readlines()

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

        # get the date in epoch time as first argument for each line
        d1 = spline[1].replace('\n', '').split(' ')

        if len(d1) == 6:
            date_s = d1[1] + ' ' + d1[2] + ' ' + d1[5]
            t1 = time.strptime(date_s, '%b %d %Y')
            t_epoch = time.mktime(t1)

        else:
            print("error")

        messages.append([str(t_epoch), 'en', spline[-1]])
        #messages.append([spline[0],'en',spline[-1]]) #include username as the first parameter

    else:
        print ("error")
        print (spline)

print (len(messages))

# write output to file

#f = open('../mallet_input/single_file/facebook/fb_comments_20160121_en.txt','w')
f = open('../../_big_files/mallet/input/twitter_streaming_space.txt','w')

for m in messages:
    f.write(' '.join(m)+'\n')

f.close()