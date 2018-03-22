import sys
from bs4 import BeautifulSoup

delete_list = ["&nbsp;", '\t', "<nobr>", "<BR>"]

with open("tales/gp-par.htm") as file:
    i = 1
    readingText = False
    fOut = open('talesText/gpOriginalMessy.txt', 'w')
    fOut2 = open('talesText/gpModernClean.txt', 'w')
    for n, line in enumerate(file):

        if line[0].isdigit() and i == int(line[0]):
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
