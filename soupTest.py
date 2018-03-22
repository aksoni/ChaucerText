from bs4 import BeautifulSoup
soup = BeautifulSoup(open("tales/gp-par.htm"), "html.parser")

#print(soup.blockquote.findAll('b'))
i = 1
fOut = open('talesText/gp2.txt', 'w')
for bq in soup.findAll('p'):
    for b in bq.findAll('b'):
    	if b.string:
        	fOut.write(b.string)
        	fOut.write('\n')

fOut.close()
		#print(i)
		#print(b.string)
		#i += 1
