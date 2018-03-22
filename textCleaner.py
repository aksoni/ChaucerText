from bs4 import BeautifulSoup
import os


#print(soup.blockquote.findAll('b'))

filesList = []

def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            if file_.endswith("_messy.txt"):
                textFileName = "talesText/" + file_
                filesList.append(textFileName)

#print(file_)
# print( os.path.join(root, file_) )

top = os.getcwd()
pywalker(top)
print(filesList)
i = 1
fOut2 = open('talesText/allOriginalText_clean.txt', 'w')
for textFile in filesList:
    soup = BeautifulSoup(open(textFile), "html.parser")
    cleanFile = textFile.split('_')[0]+"_original_clean.txt"
    fOut = open(cleanFile, 'w')
    for b in soup.findAll('b'):
        if b.string is not None:
            fOut.write(b.string)
            fOut.write('\n')
            fOut2.write(b.string)
            fOut2.write('\n')

    #print(i)
    #print(b.string)
#i += 1

    fOut.close()

fOut2.close()
		#print(i)
		#print(b.string)
		#i += 1
