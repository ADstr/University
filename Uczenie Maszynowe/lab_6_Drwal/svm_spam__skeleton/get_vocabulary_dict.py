#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import numpy as np

from typing import Dict

def get_vocabulary_dict() -> Dict[int, str]:
    import numpy as np
    filename = r"data\vocab.txt"
    with open(filename) as file:
     word=file.readlines()
    vocDict={}
    for i in range(len(word)):
     a=np.log10(i+1)
     d=int(np.floor(a))
     vocDict[i+1] = word[i][1+d:].strip()
    return vocDict
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}

