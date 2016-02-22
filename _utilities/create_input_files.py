__author__ = 'yi-linghwong'

import sys
import os


lines = open('../input/space_tweets.csv','r').readlines()
#lines = open('test.txt','r').readlines()


unique_user = []

for line in lines:
    spline = line.replace('\n','').split(',')

    if spline[0] not in unique_user:
        unique_user.append(spline[0])


print (len(unique_user))

tweets = []

for u in unique_user:
    tweets_per_user = []
    tweets_pu_combined = []

    for line in lines:
        spline = line.replace('\n','').split(',')

        if spline[0] == u:
            tweets_per_user.append(spline[1])

    # join all tweets per user into one whole tweet
    tweets_pu_combined = ' '.join(tweets_per_user)
    tweets.append(tweets_pu_combined)

print (len(tweets))

combined = zip(unique_user,tweets)
combined_list = []

for c in combined:
    c = list(c)
    combined_list.append(c)

print (len(combined_list))

for cl in combined_list:
    f = open('../input/space_tweets/'+cl[0]+'.txt','w')
    f.write(cl[1])




