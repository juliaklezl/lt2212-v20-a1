import os
import sys
import pandas as pd
import numpy as np
import numpy.random as npr
from glob import glob
# ADD ANY OTHER IMPORTS YOU LIKE

# DO NOT CHANGE THE SIGNATURES OF ANY DEFINED FUNCTIONS.
# YOU CAN ADD "HELPER" FUNCTIONS IF YOU LIKE.

def part1_load(folder1, folder2, n=2):  # I guess I can just specify that folder1 and folder2 have to be relative pathnames
    # CHANGE WHATEVER YOU WANT *INSIDE* THIS FUNCTION.
    dirname_1 = os.path.abspath("../{}".format(
        folder1))  # TODO: not sure if I need this... might be safer to get absolute path, but with ../ I also make it relative...
    dirname_2 = os.path.abspath("../{}".format(folder2))
    filenames_1 = glob("{}/*.txt".format(dirname_1))
    filenames_2 = glob("{}/*.txt".format(dirname_2))
    #alphabet = []
    data = []
    for file in filenames_1:  # there has to be a better way to get the alphabet...
        df_line = {}
        df_line['doc_name'] = file.split("/")[-1]  # TODO: name is actually path here...
        df_line['class'] = folder1  # TODO: This whole thing probably needs to be a helper function.. be careful with class label then
        with open(file, "r") as the_file:
            wholetext = the_file.readlines()
            words = []
            for line in wholetext:
                words.extend(line.split())  # TODO: This gives me a lot of numbers too... and punctuation...
            for word in words:
                #if word not in alphabet:
                 #   alphabet.append(word)
                if word in df_line:  # TODO: think about whether you should tokenize, lowercase,... etc here...
                    df_line[word] += 1
                else:
                    df_line[word] = 1
        data.append(df_line)
    df = pd.DataFrame(data)
    df = df.fillna(0)
    dx = df.sum()  # TODO: check if there is an easier way to do this - collection counter
    droplist = [i for i in list(dx.index[2:]) if dx[i] < n]
    df_dropped = df.drop(droplist, 1)
    return df_dropped

def part2_vis(df, m):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)
    # CHANGE WHAT YOU WANT HERE


    df_sum = df.sum()[2:].sort_values(ascending = False)
    df_lower = df_sum[m:]
    df_top = df.drop(df_lower.index, 1).groupby("class")
    print(df_top)
    #df_small = df.iloc[:10, :10]
    print(df_top.plot(kind="bar"))

    #df.groupby('year').case_status.value_counts().unstack(0).plot.barh()


def part3_tfidf(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    # CHANGE WHAT YOU WANT HERE
    return df #DUMMY RETURN

# ADD WHATEVER YOU NEED HERE, INCLUDING BONUS CODE.
#df = part1_load("grain", "crude")
#print(part2_vis(df, 2))

