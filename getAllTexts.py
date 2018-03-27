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

if not os.path.exists('data'):
    os.makedirs('data')

fOut = open('allText/allModernText.txt', 'w')
fOut2 = open('data/train.modern.nltkok', 'w')
fOut3 = open('data/train.original.nltkok', 'w')
fOut4 = open('data/valid.modern.nltkok', 'w')
fOut5 = open('data/test.modern.nltkok', 'w')
fOut6 = open('data/valid.original.nltkok', 'w')
fOut7 = open('data/test.original.nltkok', 'w')

#Write all modern lines to file
for textFile in modernFilesList:
    with open(textFile) as file:
        for line in file:
            fOut.write(line)
            if textFile == "wbt-par_modern_clean.txt":
                fOut4.write(line)
            elif textFile == "mlt-par_modern_clean.txt":
                fOut5.write(line)
            else:
                fOut2.write(line)
fOut.close()
fOut2.close()
fOut4.close()
fOut5.close()

fOut8 = open('allText/allOriginalText.txt', 'w')

#Write all original lines to file
for textFile in originalFilesList:
    with open(textFile) as file:
        for line in file:
            fOut8.write(line)
            if textFile == "wbt-par_original_clean.txt":
                fOut6.write(line)
            elif textFile == "mlt-par_original_clean.txt":
                fOut7.write(line)
            else:
                fOut3.write(line)

fOut3.close()
fOut6.close()
fOut7.close()
fOut8.close()


