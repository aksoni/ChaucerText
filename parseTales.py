import sys
import os
from bs4 import BeautifulSoup

delete_list = ["&nbsp;", '\t', "<nobr>", "<BR>"]

filesList = []

def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            if file_.endswith(".htm"):
                htmlFileName = "talesHTML/" + file_
                filesList.append(htmlFileName)
#print(file_)
# print( os.path.join(root, file_) )

top = os.getcwd()
pywalker(top)

print(filesList)
for htmlFile in filesList:
    with open(htmlFile) as file:
    #with open("tales/gp-par.htm") as file:
        i = 1
        readingText = False
        htmlFile = htmlFile.split('/')[1]
        originalFile = "talesText/" + htmlFile.split('.')[0] + "_original_messy.txt"
        modernFile = "talesText/" + htmlFile.split('.')[0] + "_modern_clean.txt"
        #fOut = open('talesText/gpOriginalMessy.txt', 'w')
        #fOut2 = open('talesText/gpModernClean.txt', 'w')
        fOut = open(originalFile, 'w')
        fOut2 = open(modernFile, 'w')
        for n, line in enumerate(file):

            if line[0].isdigit():# and i == int(line[0]):
                readingText = True
            
            if readingText == True and line[0].isdigit():
                fOut.write(line)
                #print("first line")
                #print(line)
            # i += 1
            elif readingText == True and line[0] is '&':
                for word in delete_list:
                   line = line.replace(word, "")
                fOut2.write(line.lstrip())
                #print("second line")
                #print(line)

        fOut.close()
        fOut2.close()
