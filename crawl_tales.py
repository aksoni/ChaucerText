import re
import urllib.request
import time
import os

#Create talesHTML directory if it does not exist
if not os.path.exists('talesHTML'):
    os.makedirs('talesHTML')

#Download HTML for each tale
for line in open('urls.txt'):
    url = line.rstrip('\n')  
    print(url)
    urlobject = urllib.request.urlopen(url)
    print(urlobject.code)
    if urlobject.code == 404:
        break

    urllib.request.urlretrieve(url, 'talesHTML/%s' % (url.split('/')[-1]))
