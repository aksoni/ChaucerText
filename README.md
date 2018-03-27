# ChaucerText

Script to extract original Canterbury Tales text and modern English sentences from interlinear translations (http://sites.fas.harvard.edu/~chaucer/teachslf/tr-index.htm).

Run sh extractText.sh to run all the necessary python files. The extracted text files are located in the allTexts directory.

talesHTML directory 
contains the HTML page for each tale, containing the original text and interlinear modern translations.

talesText directory 
contains the original and modern lines for each tale.

crawl_tales.py 
Crawls the Interlinear Translations webpages and downloads the HTML to talesHTML directory.

parseTales.py
Parses HTML files and outputs each tale's text into an original file and a modern file. The original file is "messy" because some HTML tags are still included.

textCleaner.py
Removes HTML tags from the text files containing the original lines.

getAllTexts.py
Writes all cleaned original lines to one file and all modern lines to another file into the allTexts directory.
