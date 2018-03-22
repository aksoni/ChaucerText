from bs4 import BeautifulSoup
soup = BeautifulSoup(open("gpOriginalMessy.txt"), "html.parser")

#print(soup.blockquote.findAll('b'))
i = 1
fOut = open('talesText/gp2.txt', 'w')
for b in soup.findAll('b'):
    print(i)
    print(b.string)
    i += 1

fOut.close()
		#print(i)
		#print(b.string)
		#i += 1
