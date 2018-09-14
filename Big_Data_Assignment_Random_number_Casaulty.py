
# coding: utf-8

# In[26]:


import os
import re
import io
import numpy as np
import pandas
import random
import linecache

#changing the directory to current directory
dirpath = os.getcwd()
os.chdir('C:\Users\PratikParekh\Downloads')
dirpath = os.getcwd()

random.seed(76521)
n= random.randint(1, 20)
print "The random number generated is:",n
st ="This is because of you. This yes reduces are."
with open('abs1.txt') as f:
    lines = f.readlines()[n-1:]
i=0
#print lines[i]

count =0
while i < (len(lines)-1) and count < 10:
    match = re.findall (r'[A-Z].*\breduces\b.*?\.|[A-Z].*\bbecause\b.*?\.|[A-Z].*\bincreases\b.*?\.|[A-Z].*\bdecreases\b.*?\.|[A-Z].*\baffects\b.*?\.|[A-Z].*\bcauses\b.*?\.',lines[i])
    print n+i, match
   
    if match!=[]:
        count = count +1
        
    i+=1
#print result
#print len(result)

