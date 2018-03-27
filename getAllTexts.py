import os

#Lists for the names of each downloaded HTML file
modernFilesList = []
originalFilesList = []

#Find all modern files, then create the corresponding original file name.
#This ensures that the files for each tale are in the same order in both lists.

def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            if file_.endswith("_modern_clean.txt"):
                modernFileName = "talesText/" + file_
                modernFilesList.append(modernFileName)
                originalFileName = "talesText/" + file_.split('_')[0] + "_original_clean.txt"
                originalFilesList.append(originalFileName)

top = os.getcwd()
pywalker(top)

#Creates allText directory if it does not exist
if not os.path.exists('allText'):
    os.makedirs('allText')

fOut = open('allText/allModernText.txt', 'w')

#Write all modern lines to file
for textFile in modernFilesList:
    with open(textFile) as file:
        for line in file:
            fOut.write(line)
fOut.close()


fOut2 = open('allText/allOriginalText.txt', 'w')

#Write all original lines to file
for textFile in originalFilesList:
    with open(textFile) as file:
        for line in file:
            fOut2.write(line)

fOut2.close()
