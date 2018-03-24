import os

modernFilesList = []
originalFilesList = []
def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            if file_.endswith("_modern_clean.txt"):
                modernFileName = "talesText/" + file_
                modernFilesList.append(modernFileName)
                originalFileName = "talesText/" + file_.split('_')[0] + "_original_clean.txt"
                originalFilesList.append(originalFileName)

#print(file_)
# print( os.path.join(root, file_) )

top = os.getcwd()
pywalker(top)

fOut = open('talesText/allModernText.txt', 'w')

for textFile in modernFilesList:
    with open(textFile) as file:
        for line in file:
            fOut.write(line)
fOut.close()


fOut2 = open('talesText/allOriginalText.txt', 'w')

for textFile in originalFilesList:
    with open(textFile) as file:
        for line in file:
            fOut2.write(line)

fOut2.close()

#print(modernFilesList)
#print(originalFilesList)
