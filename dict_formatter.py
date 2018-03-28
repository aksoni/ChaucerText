import os
import re

if not os.path.exists('data'):
    os.makedirs('data')

fOut = open('data/chaucer.dict', 'w')

with open("chaucer_glossary.txt") as file:
    #wordlist = [line.split(None, 1)[0] for line in file]
#print(wordlist)

    for i, line in enumerate(file):
        # print(originalList)
        print(line)
        str = line.split('\t')
        original = str[0]
        modern_messy = str[1]
        modern_messy = modern_messy.split(',')[0].rstrip()
        modern_clean = modern_messy.split(';')[0].rstrip()
            # if ',' in modern_messy:
            #modern_clean = modern_messy.split(',')[0].rstrip()
            #elif ';' in modern_messy:
            #modern_clean = modern_messy.split(';')[0].rstrip()
            #else:
            #modern_clean = modern_messy.rstrip()
            # print(modern_clean)
            #print(re.sub(r'\(.*\)', '', modern_clean))
        for word in original.split(','):
            #word = word.replace(",", "")
            word = word.lstrip()
            line = word + '\t' + modern_clean
            #print(line)
            fOut.write(line)
            fOut.write('\n')
        #modern_clean = modern_messy.split()
        # print(original)
        #  print(len(original.split()))
        # print(modern_clean)
            #for word in original.split():
            #originalList.append(word)
        #print(original)
        #print(len(original.split()))
        #str = "".join(str[1])
        #print(str[1])
        #print(str)
        #print(len(str.split()))
        #str = "".join(str[1].split(';'))
        #if len(str) > 1:
            #str = str[0]
            #else:
            #str = str.split(',')
            # print(str)
            #   print(len(str))
        
        #print(str[1])
        #if i > 30:
#   break
fOut.close()
#  break

# print(originalList)

