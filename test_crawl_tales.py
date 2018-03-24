import re
import urllib.request
import time

for line in open('urls.txt'):
    url = line.rstrip('\n')  
        #for i in range(2,10000):
    print(url)
    urlobject = urllib.request.urlopen(url)
    print(urlobject.code)
    if urlobject.code == 404:
        break

    urllib.request.urlretrieve(url, 'testTalesHTML/%s' % (url.split('/')[-1]))
