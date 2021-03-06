import os
import sys
import pandas as pd
from math import log
import numpy as np
import numpy.random as npr
from glob import glob
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# DO NOT CHANGE THE SIGNATURES OF ANY DEFINED FUNCTIONS.
# YOU CAN ADD "HELPER" FUNCTIONS IF YOU LIKE.

def part1_load(folder1, folder2, n=2):  # folder1 and folder2 need to be full paths (if folders not in same directory)
    # CHANGE WHATEVER YOU WANT *INSIDE* THIS FUNCTION.
    list1 = files_to_dictlist(folder1)
    list2 = files_to_dictlist(folder2)
    data = list1 + list2
    df = pd.DataFrame(data)
    df = df.fillna(0)
    dx = df.sum() # get sums of all columns
    droplist = [i for i in list(dx.index[2:]) if dx[i] < n] # create list of all indexes with column sums lower than n
    df_dropped = df.drop(droplist, 1)  # drop every column with words that appear less than n times in total
    return df_dropped

def files_to_dictlist(directory):  # function to get files into list of dicts for dataframe, in order to avoid duplicate code for the 2 directories
    directory_data = []
    filenames = glob("{}/*.txt".format(directory)) # get all files in given directory
    for file in filenames:
        df_line = {} # create a dict for each file that will become a row in the dataframe later
        df_line['doc_name'] = file # keeping whole path as name since some files have same name across directories
        df_line['class_name'] = directory.split("/")[-1] # class name should not be full path, only folder name
        with open(file, "r") as the_file:
            wholetext = the_file.readlines()
            words = [] # get list of all the words
            for line in wholetext:
                for word in line.split():
                    if word.isalpha(): # get rid of punctuation and numbers and lowercase all words
                        words.append(word.lower())
            for word in words:  # add new dictionary items or update existing ones
                if word in df_line:
                    df_line[word] += 1
                else:
                    df_line[word] = 1
        directory_data.append(df_line)  # add file dict to total list of rows/files
    return(directory_data)


def part2_vis(df, m):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    df_sum = df.sum()[2:].sort_values(ascending = False)  # sum all columns except for the first two (name and class)
    df_lower = df_sum[m:] # get list of all indexes ranked lower than m
    df_top = df.drop(df_lower.index, 1) # get rid of all columns that are not in top m
    df_top_grouped = df_top.groupby(['class_name']).sum().sort_values(df_top['class_name'][0], axis=1, ascending = False) # plot top m words, sorted according to first classname, here grain
    return df_top_grouped.T.plot(kind="bar")


def part3_tfidf(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    df2 = df.copy()  # create independent copy of df, so that original df doesnt get changed
    for column in df2:
        if column != "doc_name" and column != "class_name":  # exclude columns without numerical values
            zeros = df2[column].isin([0]).sum() # get number of articles without word
            idf = len(df2)/(len(df2) - zeros) # number of articles / number of articles including word
            df2[column] = df2[column] * log(idf)  # multiply all raw counts in the column with the log of idf.
    return df2

def train_and_evaluate(df):
    model = SVC(gamma = "auto", kernel="rbf") # create model
    x = df.drop(["class_name", "doc_name"], 1) # choose x data
    y = df["class_name"] # choose y data
    model.fit(x, y) # train model
    y_pred = model.predict(x) # predict and evaluate:
    print(confusion_matrix(y, y_pred))
    print(classification_report(y, y_pred))
    return accuracy_score(y, y_pred)
