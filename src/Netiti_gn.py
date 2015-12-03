#!/usr/bin/env python
from neti_neti_trainer import NetiNetiTrainer
from neti_neti import NetiNeti
import subprocess
import shlex
import math
import sys
import time
import os
import difflib

import fio

datadir = "../../good-bad-names-for-GN/data/"

import time
time_start = time.clock()

import pickle
classifier = NetiNetiTrainer(learning_algorithm='NB')
with open('classifier_NB.pickle', 'wb') as handle:
    pickle.dump(classifier, handle)
#  exit(-1)

with open('classifier_NB.pickle', 'rb') as handle:
    classifier = pickle.load(handle)

nn = NetiNeti(classifier)

time_traning = time.clock()
print "training time: %s" % (time_traning - time_start)

time_start = time.clock()

input = datadir + 'all_name_strings.txt'
output = datadir + 'all_name_strings.NetiNeti'

import codecs

fout = codecs.open(output, 'w', 'utf-8')

results = []
for line in codecs.open(input, 'r', 'utf-8'):
    line = line.strip()
    result = nn.find_names(line)
    name = result[0]
    
    if len(name) == 0:
        fout.write('No\r\n')
    elif name != line:
        fout.write('YesNo\r\n')
    else:
        fout.write('Yes\r\n')

fout.close()

time_decoding = time.clock()
print "decoding time: %s" % (time_decoding - time_start)