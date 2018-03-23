import sys
import os
from bs4 import BeautifulSoup

delete_list = ["&nbsp;", "nbsp;", '\t', "<nobr>", "<BR>", "</B>", "<i>", "</i>", "<br>", "</b>"]

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
#fOut3 = open('talesText/allOriginalText_messy.txt', 'w')
fOut4 = open('talesText/allModernText_clean.txt', 'w')
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
            #print(htmlFile)
            #if htmlFile == "sqt-par.htm" and readingText == True:
            #   print(line.lstrip()[0:3])
            if line[0].isdigit():# and i == int(line[0]):
                readingText = True
            
            if readingText == True and len(line.lstrip()) > 0 and line.lstrip()[0].isdigit():
                line = line.replace(">/b>", "</b>")
                fOut.write(line)
            #fOut3.write(line)
                #print("first line")
                #print(line)
            # i += 1
            elif readingText == True and (line[0] is 'n' or (len(line.lstrip()) > 0 and (line.lstrip()[0] == '&' or line.lstrip()[0:4] == 'A pe' or line.lstrip()[0:4] == 'A lo' or
                                                                                         line.lstrip()[0] == 'n' or line.lstrip()[0:3] == 'and' or line.lstrip()[0:4] == '</B>' or line.lstrip()[0:4] == '</b>'))):#line[0] is '&' or line[0] is ' &' or (len(line.lstrip()) > 0 and line.lstrip()[0] == '&'):
                for word in delete_list:
                    line = line.replace(word, "")
                if line.lstrip()[0:11] == "Immediately":
                    fOut2.write("Immediately this tiger, full of treachery," + '\n')
                    fOut4.write("Immediately this tiger, full of treachery," + '\n')
                elif line.lstrip()[0:4] != "[The" and line.lstrip()[0:3] != "<i>" and line.lstrip()[0:3] != "<b>" and line.lstrip()[0:3] != "[Ze" and line.lstrip()[0:3] != "[Ne" and line.lstrip()[0:3] != "[Co" and line.lstrip()[0:3] != "</F" and line.lstrip()[0:9] != "Invocacio" and line.lstrip()[0:9] != "(Invocati" and line.lstrip()[0:13] != "Interpretacio" and line.lstrip()[0:9] != "(The inte" and line.lstrip()[0:10] != "Jacobus Ja" and line.lstrip()[0:10] != "Jacob of G" and line.lstrip()[0:8] != "Explicit" and line.lstrip()[0:8] != "(Here en" and line.lstrip()[0:3] != "[Pr" and line.lstrip()[0:3] != "[[F" and line.lstrip()[0:11] != "And tell fo":
                    fOut2.write(line.lstrip())
                    fOut4.write(line.lstrip())
                if line.lstrip()[0:20] == "And did stand before":
                    fOut2.write("Valerian as if dead fell down for fear" + '\n')
                    fOut4.write("Valerian as if dead fell down for fear" + '\n')
                #print("second line")
                #print(line)

        fOut.close()
        fOut2.close()

#fOut3.close()
fOut4.close()
