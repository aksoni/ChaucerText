from bs4 import BeautifulSoup
import os


#print(soup.blockquote.findAll('b'))

filesList = []
delete_list = ["&nbsp;", "nbsp;", '\t', "<nobr>", "<BR>", "</B>"]
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
#print(filesList)
i = 1
fOut2 = open('talesText/allOriginalText_clean.txt', 'w')
for textFile in filesList:
    cleanFile = textFile.split('_')[0]+"_original_clean.txt"
    fOut = open(cleanFile, 'w')
    
    if textFile == "talesText/sqt-par_original_messy.txt":
        with open(textFile) as file:
            for line in file:
                #print(line)
                line = line.split('<B>')[1]
                #print(line)
                for word in delete_list:
                    line = line.replace(word, "")
                #print(line)
                fOut.write(line)
                fOut.write('\n')
                fOut2.write(line)
                fOut2.write('\n')
        break;
    soup = BeautifulSoup(open(textFile), "html.parser")

    #print(textFile)
   
    for b in soup.findAll('b'):
        #b.getText()
        if b.string is not None:
            fOut.write(b.string.lstrip())
            fOut.write('\n')
            fOut2.write(b.string.lstrip())
            fOut2.write('\n')
        elif b.getText() is not None:
            fOut.write(b.getText().lstrip())
            fOut.write('\n')
            fOut2.write(b.getText().lstrip())
            fOut2.write('\n')
    
        

    #print(i)
    #print(b.string)
#i += 1

    fOut.close()

fOut2.close()
		#print(i)
		#print(b.string)
		#i += 1
