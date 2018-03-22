from bs4 import BeautifulSoup
soup = BeautifulSoup(open("gpOriginalMessy.txt"), "html.parser")

#print(soup.blockquote.findAll('b'))
i = 1
fOut = open('talesText/gpOriginalClean.txt', 'w')
for b in soup.findAll('b'):
    fOut.write(b.string)
    fOut.write('\n')
    #print(i)
    #print(b.string)
#i += 1

fOut.close()
		#print(i)
		#print(b.string)
		#i += 1
