__author__ = 'yi-linghwong'

import sys
import os

#################
# create one file per user for Gephi input
# combine all tweets of that user into one paragraph
#################


path_to_preprocessed_data_file = '../../FacebookML/fb_data/posts/preprocessed_fb_posts_20160223.csv'
path_to_store_output_directory = '../mallet_input/multiple_files/fb_posts/'

lines = open(path_to_preprocessed_data_file,'r').readlines()
#lines = open('test.txt','r').readlines()


unique_user = []

for line in lines:
    spline = line.replace('\n','').split(',')

    if spline[0] not in unique_user:
        unique_user.append(spline[0])


print ("Number of user is "+str(len(unique_user)))

texts = []

for u in unique_user:
    texts_per_user = []
    texts_pu_combined = []

    for line in lines:
        spline = line.replace('\n','').split(',')

        if spline[0] == u:
            texts_per_user.append(spline[-1])

    # join all tweets per user into one whole tweet
    texts_pu_combined = ' '.join(texts_per_user)
    texts.append(texts_pu_combined)

print ("Length of text is "+str(len(texts)))

combined = zip(unique_user,texts)
combined_list = []

for c in combined:
    c = list(c)
    combined_list.append(c)

print ("Length of combined list is "+str(len(combined_list)))

for cl in combined_list[1:]:
    f = open(path_to_store_output_directory+cl[0]+'.txt','w')
    f.write(cl[1])




