__author__ = 'yi-linghwong'

###############
# methods for tweet and fb post preprocessing, includes:
# remove URL, RT, mention, special characters, stopwords, remove all of the above ('cleanup') plus single characters
###############

import re
import os
import sys
import itertools
#from nltk.corpus import stopwords
from sklearn.feature_extraction import text

lines = open('../../TwitterML/stopwords/stopwords.csv', 'r').readlines()

my_stopwords=[]
for line in lines:
    my_stopwords.append(line.replace("\n", ""))

stop_words = text.ENGLISH_STOP_WORDS.union(my_stopwords)


class MessageProcessing():

    def get_element_number_per_line(self):

        lines = open(path_to_raw_msg_file,'r').readlines()

        print (len(lines))

        for line in lines[:1]:
            spline = line.replace('\n','').split(',')

        length = len(spline)

        return length


    def remove_url_mention_hashtag(self):

        lines = open(path_to_raw_msg_file,'r').readlines()

        messages = []
        for line in lines:

            spline = line.replace('\n','').split(',')
            messages.append(spline)

        msg_list = []

        length = self.get_element_number_per_line()

        print ("Removing url, mentions and hashtags...")

        for m in messages:

            if (len(m)) == length:

                m1 = m[-1]

                #remove URLs
                m2 = re.sub(r'(?:https?\://)\S+', '', m1)

                #remove mentions
                m3 = re.sub(r'(?:\@)\S+', '', m2)

                #remove hashtags (just the symbol, not the key word)

                m4 = re.sub(r"#","", m3).strip()

                m5 = m4.lower()

                m[-1] = ' '+m5+' '

                msg_list.append(m)

            else:
                print ("error")
                print (m)

        print (len(msg_list))

        return msg_list


    def remove_punctuations(self):

        # Replace punctuation with white space, not nil! So that words won't join together when punctuation is removed

        messages = self.remove_url_mention_hashtag()

        msg_list = []

        print ("Removing punctuations ...")

        for m in messages:

            #remove special characters
            m1 = re.sub("[^A-Za-z0-9]+",' ', m[-1])
            m[-1] = m1

            msg_list.append(m)

        print (len(msg_list))

        return msg_list


    def expand_contractions(self):

        contractions_dict = {
            ' isn\'t ': ' is not ',
            ' isn’t ': ' is not ',
            ' isnt ': ' is not ',
            ' isn ': ' is not ',
            ' aren\'t ': ' are not ',
            ' aren’t ': ' are not ',
            ' arent ': ' are not ',
            ' aren ': ' are not ',
            ' wasn\'t ': ' was not ',
            ' wasn’t ': ' was not ',
            ' wasnt ': ' was not ',
            ' wasn ': ' was not ',
            ' weren\'t ': ' were not ',
            ' weren’t ': ' were not ',
            ' werent ': ' were not ',
            ' weren ': ' were not ',
            ' haven\'t ': ' have not ',
            ' haven’t ': ' have not ',
            ' havent ': ' have not ',
            ' haven ': ' have not ',
            ' hasn\'t ': ' has not ',
            ' hasn’t ': ' has not ',
            ' hasnt ': ' has not ',
            ' hasn ': ' has not ',
            ' hadn\'t ': ' had not ',
            ' hadn’t ': ' had not ',
            ' hadnt ': ' had not ',
            ' hadn ': ' had not ',
            ' won\'t ': ' will not ',
            ' won’t ': ' will not ',
            ' wouldn\'t ': ' would not ',
            ' wouldn’t ': ' would not ',
            ' wouldnt ': ' would not ',
            ' wouldn ': ' would not ',
            ' didn\'t ': ' did not ',
            ' didn’t ': ' did not ',
            ' didnt ': ' did not ',
            ' didn ': ' did not ',
            ' don\'t ': ' do not ',
            ' don’t ': ' do not ',
            ' dont ': ' do not ',
            ' don ': ' do not ',
            ' doesn\'t ': ' does not ',
            ' doesn’t ': ' does not ',
            ' doesnt ': ' does not ',
            ' doesn ': ' does not ',
            ' can\'t ': ' can not ',
            ' can’t ': ' can not ',
            ' cant ': ' can not ',
            ' couldn\'t ': ' could not ',
            ' couldn’t ': ' could not ',
            ' couldnt ': ' could not ',
            ' couldn ': ' could not ',
            ' shouldn\'t ': ' should not ',
            ' shouldn’t ': ' should not ',
            ' shouldnt ': ' should not ',
            ' shouldn ': ' should not ',
            ' mightn\'t ': ' might not ',
            ' mightn’t ': ' might not ',
            ' mightnt ': ' might not ',
            ' mightn ': ' might not ',
            ' mustn\'t ': ' must not ',
            ' mustn’t ': ' must not ',
            ' mustnt ': ' must not ',
            ' mustn ': ' must not ',
            ' shan\'t ': ' shall not ',
            ' shan’t ': ' shall not ',
            ' shant ': ' shall not ',
            ' shan ': ' shall not ',
        }

        messages = self.remove_punctuations()
        msg_list = []

        contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()), re.IGNORECASE)

        def replace(match):

            return contractions_dict[match.group(0).lower()]

        print ("Expanding contractions ...")

        for m in messages:

            m1 = contractions_re.sub(replace, m[-1])
            m[-1] = m1
            msg_list.append(m)

        print (len(msg_list))

        return msg_list


    def remove_stopwords(self):

        messages = self.expand_contractions()

        msg_list=[]

        print ("Removing stopwords ...")

        for m in messages:
            no_stop=[] #important

            for w in m[-1].split():
                #remove single characters and stop words
                if (len(w.lower())>=2) and (w.lower() not in stop_words):
                    no_stop.append(w.lower())


                    #join the list of words together into a string
                    m[-1] = " ".join(no_stop)

            msg_list.append(m)

        print (len(msg_list))

        return msg_list


    def remove_rt(self):

    #############
    # remove the term 'rt'
    #############

        messages = self.remove_stopwords()

        msg_list = []

        print ("Removing rt...")

        for m in messages:

            # add blank space before and after tweet so that if sentence starts with rt it can be detected (e.g. 'rt @nasa blah blah')
            m1 = ' '+m[-1]+' '
            m2 = m1.replace(' rt ',' ')
            m[-1] = m2

            msg_list.append(m)

        print (len(msg_list))

        return msg_list


    def remove_duplicate(self):

        messages = self.remove_rt()

        msg_list = []
        temp = []

        print ("Removing duplicates...")

        for m in messages:
            if m[-1] not in temp:
                temp.append(m[-1])
                msg_list.append(m)

        print (len(msg_list))

        return msg_list


    def remove_empty_lines(self):

        messages = self.remove_rt()

        msg_list = []

        print ("Removing empty lines...")

        for m in messages:

            if m[-1] == '   ':
                m[-1] = ' null '
                msg_list.append(m)

            else:
                msg_list.append(m)


        print (len(msg_list))

        return msg_list


    def write_to_file(self):

        messages = self.remove_empty_lines()
        length = self.get_element_number_per_line()

        print ("Number of element per line is "+str(length))

        f = open(path_to_store_processed_msg_file,'w')

        print ("Writing to file ...")

        for m in messages:
            if (len(m)) == length:

                f.write(','.join(m)+'\n')

            else:
                print ("error")
                print (m)

        f.close()

        return


###############
# variables
###############

#path_to_raw_msg_file = '../../FacebookML/fb_data/comments/raw_fb_comments_20160121_en.csv'
path_to_raw_msg_file = '../../_big_files/facebook/raw_fb_comments_replies_20160223_en.csv'

#path_to_store_processed_msg_file = '../mallet_input/preprocessed_files/facebook/preprocessed_fb_comments_20160121_en.csv'
path_to_store_processed_msg_file = '../../_big_files/facebook/preprocessed_fb_comments_replies_20160223_en.csv'

if __name__ == "__main__":

    mp = MessageProcessing()

    mp.write_to_file()





