
# coding: utf-8

# In[11]:


import os
import re
import io
import numpy as np
import pandas
dirpath = os.getcwd()
os.chdir('C:\Users\PratikParekh\Downloads')


textfile = open('abs1.txt', 'r')
filetext = textfile.read()
textfile.close()
pattern = re.compile(r"\n")
matches=pattern.findall(filetext)
n=len(matches)
print "Number of matches of \n :",n
result=pattern.split(filetext)



for i in xrange(len(result)-1):
    p=result[i]
    with io.open("pratik_" + str(i) + ".txt", 'w',encoding='utf-8') as f:
        f.write(unicode(p))


i=0

textfile = open ('pratik_'+str(i) +'.txt','r')
filetext = textfile.read()
textfile.close()
pattern = re.compile(r"consumers|investors|stakeholders")
match = pattern.findall(filetext)
n = len(match)
x = match.count("consumers")
y = match.count("investors")
z = match.count("stakeholders")
s = ['pratik_' +str(i)]
data = np.array([[match.count("consumers"),match.count("investors"),match.count("stakeholders")]])


for i in xrange(1,len(result)-1):
    textfile = open ('pratik_'+str(i) +'.txt','r')
    filetext = textfile.read()
    textfile.close()
    pattern = re.compile(r"consumers|investors|stakeholders")
    match = pattern.findall(filetext)
    n = len(match)
    s.append('pratik_'+str(i))
    data1=np.array([[match.count("consumers"),match.count("investors"),match.count("stakeholders")]])
    
    data=np.append(data,data1)
#print(s)
#print(data)

data = data.reshape(865,3)



pandas.DataFrame(data, s, columns=['consumers','investers','stakeholders'])

