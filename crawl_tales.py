import re
import urllib.request
import time
import os

if not os.path.exists('talesHTML'):
    os.makedirs('talesHTML')

for line in open('urls.txt'):
    url = line.rstrip('\n')  
    print(url)
    urlobject = urllib.request.urlopen(url)
    print(urlobject.code)
    if urlobject.code == 404:
        break

    urllib.request.urlretrieve(url, 'talesHTML/%s' % (url.split('/')[-1]))
