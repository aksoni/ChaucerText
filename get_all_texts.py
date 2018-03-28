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

#Creates data directory if it does not exist
if not os.path.exists('data'):
    os.makedirs('data')

#Open files in which to write lines
fOut = open('allText/allModernText.txt', 'w')
fOut2 = open('data/train.modern.nltkok', 'w')
fOut3 = open('data/train.original.nltkok', 'w')
fOut4 = open('data/valid.modern.nltkok', 'w')
fOut5 = open('data/test.modern.nltkok', 'w')
fOut6 = open('data/valid.original.nltkok', 'w')
fOut7 = open('data/test.original.nltkok', 'w')




for textFile in modernFilesList:
    with open(textFile) as file:
        for line in file:
            #Write all modern lines to allText file
            fOut.write(line)
            
            if textFile == "talesText/wbt-par_modern_clean.txt":
                #Write Wife of Bath's tale to validation file
                fOut4.write(line)
            
            elif textFile == "talesText/mlt-par_modern_clean.txt":
                #Write Man of Law's tale to test file
                fOut5.write(line)
            
            else:
                #Write all other tales to training file
                fOut2.write(line)
fOut.close()
fOut2.close()
fOut4.close()
fOut5.close()

fOut8 = open('allText/allOriginalText.txt', 'w')


for textFile in originalFilesList:
    with open(textFile) as file:
        for line in file:
            #Write all original lines to file
            fOut8.write(line)
            
            if textFile == "talesText/wbt-par_original_clean.txt":
                #Write Wife of Bath's tale to validation file
                fOut6.write(line)
            
            elif textFile == "talesText/mlt-par_original_clean.txt":
                #Write Man of Law's tale to test file
                fOut7.write(line)
            
            else:
                #Write all other tales to training file
                fOut3.write(line)

fOut3.close()
fOut6.close()
fOut7.close()
fOut8.close()


