import re
import urllib.request
import time

for line in open('urls.txt'):
    url = line.rstrip('\n')  
    for i in range(2,10000):
        print(url)
        urlobject = urllib.request.urlopen(url)
        print(urlobject.code)
        if urlobject.code == 404:
            break
# resource = urllib.request.urlopen(an_url)
#content =  resource.read().decode(resource.headers.get_content_charset())
#lines = urllib.request.urlopen(url).read().decode(urlobject.headers.get_content_charset())


        content =  urlobject.readlines().decode('utf-8')
        fOut = open('testTalesHTML/%s' % (url.split('/')[-1]), 'w')

        fOut.write("\n".join(content))
        fOut.close()
        time.sleep(1)


        #Get the next URL
        url = None
        for line in content:
            m = re.match(r'<div class="next"><a href="(.+)">Next Section', line)
            if m:
                url = m.group(1)
                print(url)
                break

        if not url:
            break
