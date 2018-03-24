from bs4 import BeautifulSoup
import os


filesList = []
delete_list = ["&nbsp;", "nbsp;", '\t', "<nobr>", "<BR>", "<br>","</b>", "</B>"]
def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            if file_.endswith("_messy.txt"):
                textFileName = "talesText/" + file_
                filesList.append(textFileName)


top = os.getcwd()
pywalker(top)

for textFile in filesList:
    cleanFile = textFile.split('_')[0]+"_original_clean.txt"
    fOut = open(cleanFile, 'w')
    
    if textFile == "talesText/sqt-par_original_messy.txt" or textFile == "talesText/mkt-par_original_messy.txt":
       
        with open(textFile) as file:
            for line in file:
                
                line = line.split('<B>')[1]
                
                for word in delete_list:
                    line = line.replace(word, "")
                
                fOut.write(line.lstrip())

    else:
        soup = BeautifulSoup(open(textFile), "html.parser")



        for b in soup.findAll('b'):
            
            if b.string is not None:
                fOut.write(b.string.lstrip())
                fOut.write('\n')
            
            elif b.getText() is not None:
                fOut.write(b.getText().lstrip())
                fOut.write('\n')


    fOut.close()

