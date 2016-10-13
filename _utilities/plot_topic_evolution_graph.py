__author__ = 'yi-linghwong'

import sys
import os
import matplotlib.pyplot as plt
import pylab
import time
import matplotlib.dates as mdates

class PlotTopicGraph():

    def __init__(self):

        print ("Welcome...")

        print ()

    def get_topic_proportions(self):

        lines = open(path_to_composition_file,'r').readlines()

        date_list = []

        for line in lines[1:]:

            spline = line.rstrip('\n').split('\t')

            if spline[1] not in date_list:
                date_list.append(spline[1])

        print("Length of date list is " + str(len(date_list)))

        topic_proportion_dict = {}

        for dl in date_list:

            topic_proportion_list = []

            for line in lines[1:]:

                spline = line.rstrip('\n').split('\t')

                if spline[1] == dl:

                    for n in range(2,22,2):

                        if float(spline[n+1]) > 0.35: #only include topic proportions that are bigger than 35%
                            topic_proportion_list.append([spline[n],spline[n+1]])


            topic_proportion_dict[dl] = topic_proportion_list

        print("Length of topic proportion dictionary is " + str(len(topic_proportion_dict)))

        return date_list,topic_proportion_dict


    def plot_topic_graph(self):

        date_and_topic_lists = self.get_topic_proportions()

        date_list = date_and_topic_lists[0]
        topic_proportion_dict = date_and_topic_lists[1]

        ###################
        # create a dictionary with topic and the number of tweets that contain it
        # i.e. { date1:[[topic_0, 3], [topic_1, 4],...], date2:[[topic_0, 5], [topic_1, 1],...]
        ###################

        topic_count_dict = {}

        print ()
        print ("Computing topic counts ...")

        for date,value in topic_proportion_dict.items():

            topic_count = []

            for n in range(0,10): # n is the topic number

                count = 0

                for v in value:
                    if int(v[0]) == n:
                        count += 1

                topic_count.append([n,count])

            topic_count_dict[date] = topic_count

        #print (topic_count_dict)

        #topic_list = [0,1,2,3,4,5,6,7,8,9]
        topic_list = [0]
        topic_names = ['0_astronomy_love','1_spacex_mars_mission','2_international_space_station',
                       '3_astrobiology','4_??', '5_zodiac_sign_change','6_hurricane_matthews',
                       '7_NASA_news','8_rosetta_mission_end','9_europa_plumes']

        for tl in topic_list:

            dates = []
            counts = []

            for date,value in topic_count_dict.items():

                dates.append(float(date))

                for v in value:

                    if v[0] == tl:

                        counts.append(v[1])

            if len(dates) == len(counts):

                zipped = zip(dates,counts)

                dates_counts = []

                for z in zipped:
                    z = list(z)
                    dates_counts.append(z)


            else:
                print ("Length of lists not equal, exiting...")

                sys.exit()

            # sort list by date
            dates_counts.sort(key=lambda x: x[0])

            dates_x = []
            counts_y = []

            for dc in dates_counts:

                dates_x.append(dc[0])
                counts_y.append(dc[1])

            print (dates_x)
            print (counts_y)

            secs = mdates.epoch2num(dates_x)

            fig, ax = plt.subplots()

            # Plot the date using plot_date rather than plot
            ax.plot_date(secs, counts_y, linestyle='-', marker='*', label='Topic_'+str(tl))

            # Choose your xtick format string
            date_fmt = '%d-%m-%y'

            # Use a DateFormatter to set the data to the correct format.
            date_formatter = mdates.DateFormatter(date_fmt)
            ax.xaxis.set_major_formatter(date_formatter)

            # Sets the tick labels diagonal so they fit easier.
            fig.autofmt_xdate()

            pylab.legend(loc='upper left')
            plt.xlabel('Date')
            plt.ylabel('Tweet count')

            plt.show()


            # plt.plot(dates_x, counts_y, linestyle='-', marker='*', label='Topic_'+str(tl))
            #
            # plt.gcf().autofmt_xdate()
            #
            # formatter = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
            # plt.gcf().xaxis.set_major_formatter(formatter)
            #
            # pylab.legend(loc='upper left')
            # plt.xlabel('Epoch time')
            # plt.ylabel('Tweet count')
            #
            # plt.show()


#################
# variables
#################

path_to_composition_file = '/Users/yi-linghwong/GitHub/_big_files/mallet/composition_file/streaming_space_composition.txt'
#path_to_composition_file = '/Users/yi-linghwong/GitHub/_big_files/mallet/composition_file/test.txt'


if __name__ == '__main__':

    pt = PlotTopicGraph()

    #pt.get_topic_proportions()
    pt.plot_topic_graph()

