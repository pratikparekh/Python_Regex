
# coding: utf-8

# In[4]:





# In[36]:


import urllib
import urllib2
import random

from bs4 import BeautifulSoup

random.seed(521)
n= random.randint(1, 20)
print "The random number generated is:",n 


textToSearch = 'Simple Linear Regression'
query = urllib.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})
link= vid[n-1]
print "The youtube line is " + 'https://www.youtube.com' + link['href']


