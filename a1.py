import os
import sys
import pandas as pd
import numpy as np
import numpy.random as npr
from glob import glob
# ADD ANY OTHER IMPORTS YOU LIKE

# DO NOT CHANGE THE SIGNATURES OF ANY DEFINED FUNCTIONS.
# YOU CAN ADD "HELPER" FUNCTIONS IF YOU LIKE.

def part1_load(folder1, folder2, n=2):  # folder1 and folder2 need to be full paths (if folders not in same directory)
    # CHANGE WHATEVER YOU WANT *INSIDE* THIS FUNCTION.
    list1 = files_to_dictlist(folder1)
    list2 = files_to_dictlist(folder2)
    data = list1 + list2
    df = pd.DataFrame(data)
    df = df.fillna(0)
    dx = df.sum()
    droplist = [i for i in list(dx.index[2:]) if dx[i] < n]
    df_dropped = df.drop(droplist, 1)
    return df_dropped

def files_to_dictlist(directory):  # function to get files into list of dicts for dataframe, in order to avoid duplicate code for the 2 directories
    directory_data = []
    filenames = glob("{}/*.txt".format(directory))
    for file in filenames:
        df_line = {}
        df_line['doc_name'] = file # keeping whole path as name since some files have same name across directories
        df_line['class_name'] = directory.split("/")[-1] # class name should not be full path, only folder name
        with open(file, "r") as the_file:
            wholetext = the_file.readlines()
            words = []
            for line in wholetext:
                for word in line.split():
                    if word.isalpha(): # get rid of punctuation and numbers and lowercase all words
                        words.append(word.lower())
            for word in words:
                if word in df_line:  # TODO: tokenize???
                    df_line[word] += 1
                else:
                    df_line[word] = 1
        directory_data.append(df_line)
    return(directory_data)
    df = pd.DataFrame(data)
    df = df.fillna(0)
    dx = df.sum()
    droplist = [i for i in list(dx.index[2:]) if dx[i] < n]
    df_dropped = df.drop(droplist, 1)
    return df_dropped

def part2_vis(df, m):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)
    # CHANGE WHAT YOU WANT HERE
    df_sum = df.sum()[2:].sort_values(ascending = False)
    df_lower = df_sum[m:]
    df_top = df.drop(df_lower.index, 1) # get rid of all columns that are not in top m
    df_top_grouped = df_top.groupby(['class_name']).sum()
    print(df_top_grouped)
    print(df_top_grouped.T.plot(kind="bar"))

    #df.groupby('year').case_status.value_counts().unstack(0).plot.barh()


def part3_tfidf(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    # CHANGE WHAT YOU WANT HERE
    return df #DUMMY RETURN

# ADD WHATEVER YOU NEED HERE, INCLUDING BONUS CODE.
#df = part1_load("grain", "crude")
#print(part2_vis(df, 2))

