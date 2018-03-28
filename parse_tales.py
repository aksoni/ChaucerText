import sys
import os
from bs4 import BeautifulSoup

#List of symbols to delete from extracted lines
delete_list = ["&nbsp;", "nbsp;", '\t', "<nobr>", "<BR>", "</B>", "<i>", "</i>", "<br>", "</b>"]

filesList = []

#Find all downloaded HTML files
def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            if file_.endswith(".htm"):
                htmlFileName = "talesHTML/" + file_
                filesList.append(htmlFileName)

top = os.getcwd()
pywalker(top)

#Create talesText directory if it does not exist
if not os.path.exists('talesText'):
    os.makedirs('talesText')

for htmlFile in filesList:
    with open(htmlFile) as file:

        readingText = False #Only start reading lines if the first line of actual text has been encountered
        
        #Create names for the original and modern text files
        htmlFile = htmlFile.split('/')[1]
        originalFile = "talesText/" + htmlFile.split('.')[0] + "_original_messy.txt"
        modernFile = "talesText/" + htmlFile.split('.')[0] + "_modern_clean.txt"

        fOut = open(originalFile, 'w')
        fOut2 = open(modernFile, 'w')
        
        #Write lines to original and modern file
        for n, line in enumerate(file):
            
            #All original lines start with the line number
            if line[0].isdigit():
                readingText = True
            
            #Write original line to file
            if readingText == True and len(line.lstrip()) > 0 and line.lstrip()[0].isdigit():
                line = line.replace(">/b>", "</b>")      #Fixes typo in tag found in an HTML file of one of the tales
                fOut.write(line)
            
            #If the line is a modern translation, the HTML line will match these conditions
            elif readingText == True and (line[0] is 'n' or (len(line.lstrip()) > 0 and (line.lstrip()[0] == '&' or line.lstrip()[0:4] == 'A pe' or line.lstrip()[0:4] == 'A lo' or
                                                                                         line.lstrip()[0] == 'n' or line.lstrip()[0:3] == 'and' or line.lstrip()[0:4] == '</B>' or line.lstrip()[0:4] == '</b>'))):
                #Cleans the modern text
                for word in delete_list:
                    line = line.replace(word, "")
                
                #A formatting error in the HTML prevents proper extraction of this line. Therefore, manually writing is necessary.
                if htmlFile == "sqt-par.htm" and line.lstrip()[0:11] == "Immediately":
                    fOut2.write("Immediately this tiger, full of treachery," + '\n')
     
                #Some HTML lines match the conditions for the parent elif, but should not be written to file. This checks for any condition that shows that the line should not be written to file.
                elif line.lstrip()[0:4] != "[The" and line.lstrip()[0:3] != "<i>" and line.lstrip()[0:3] != "<b>" and line.lstrip()[0:3] != "[Ze" and line.lstrip()[0:3] != "[Ne" and line.lstrip()[0:3] != "[Co" and line.lstrip()[0:3] != "</F" and line.lstrip()[0:9] != "Invocacio" and line.lstrip()[0:9] != "(Invocati" and line.lstrip()[0:13] != "Interpretacio" and line.lstrip()[0:9] != "(The inte" and line.lstrip()[0:10] != "Jacobus Ja" and line.lstrip()[0:10] != "Jacob of G" and line.lstrip()[0:8] != "Explicit" and line.lstrip()[0:8] != "(Here en" and line.lstrip()[0:3] != "[Pr" and line.lstrip()[0:3] != "[[F" and line.lstrip()[0:11] != "And tell fo":
                    fOut2.write(line.lstrip())
                
                #A formatting error in the HTML prevents proper extraction of this line. Therefore, manually writing is necessary.
                if line.lstrip()[0:20] == "And did stand before":
                    fOut2.write("Valerian as if dead fell down for fear" + '\n')

        fOut.close()
        fOut2.close()

