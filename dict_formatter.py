import os
import re

if not os.path.exists('data'):
    os.makedirs('data')

fOut = open('data/chaucer.dict', 'w')

with open("chaucer_glossary.txt") as file:

    for i, line in enumerate(file):
        
        print(line)
        
        str = line.split('\t')
        
        original = str[0]
        
        modern_messy = str[1]
        modern_messy = modern_messy.split(',')[0].rstrip()
        modern_clean = modern_messy.split(';')[0].rstrip()
     
        for word in original.split(','):
            
            word = word.lstrip()
            word = word.rstrip()
            line = word + '\t' + modern_clean
    
            fOut.write(line)
            fOut.write('\n')

fOut.close()
