import sys
from bs4 import BeautifulSoup

with open("tales/gp-par.htm") as file:
    i = 1
    readingText = False
    for n, line in enumerate(file):

        if line[0].isdigit() and i == int(line[0]):
            readingText = True
        
        if readingText == True and line[0].isdigit():
    	    print("first line")
    	    print(line)
        # i += 1
        elif readingText == True and line[0] is '&':
            print("second line")
            print(line)

