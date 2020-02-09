import os
import sys
import pandas as pd
import numpy as np
import numpy.random as npr
from glob import glob
# ADD ANY OTHER IMPORTS YOU LIKE

# DO NOT CHANGE THE SIGNATURES OF ANY DEFINED FUNCTIONS.
# YOU CAN ADD "HELPER" FUNCTIONS IF YOU LIKE.

def part1_load(folder1, folder2):
    dirname_1 = os.path.abspath("../{}".format(folder1)) # not sure if I need this... might be safer to get absolute path, but with ../ I also make it relative...
    dirname_2 = os.path.abspath("../{}".format(folder2))
    filenames_1 = glob("{}/*.txt".format(dirname_1))
    filenames_2 = glob("{}/*.txt".format(dirname_2))
    for file in filenames_1:
        print(file)
        with open (file, "r") as the_file:
            the_file.read()

def part1_load(folder1, folder2, n=1):
    # CHANGE WHATEVER YOU WANT *INSIDE* THIS FUNCTION.
    return pd.DataFrame(npr.randn(2,2)) # DUMMY RETURN

def part2_vis(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    # CHANGE WHAT YOU WANT HERE
    return df.plot(kind="bar")

def part3_tfidf(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    # CHANGE WHAT YOU WANT HERE
    return df #DUMMY RETURN

# ADD WHATEVER YOU NEED HERE, INCLUDING BONUS CODE.

part1_load("grain", "crude")

