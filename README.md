# ChaucerText

Script to extract original Canterbury Tales text and modern English sentences from interlinear translations (http://sites.fas.harvard.edu/~chaucer/teachslf/tr-index.htm).

Run sh extractText.sh to run all the necessary python files. The extracted text files are located in the allTexts directory.

talesHTML directory 
contains the HTML page for each tale, containing the original text and interlinear modern translations.

talesText directory 
contains the original and modern lines for each tale.

data directory
contains the training, validation, and testing files for both original and modern sentences, as well as a baseline dictionary for commonly used words in Chaucer's works.

crawl_tales.py 
Crawls the Interlinear Translations webpages and downloads the HTML to talesHTML directory.

parse_tales.py
Parses HTML files and outputs each tale's text into an original file and a modern file. The original file is "messy" because some HTML tags are still included.

text_cleaner.py
Removes HTML tags from the text files containing the original lines.

get_all_texts.py
Writes all cleaned original lines to one file and all modern lines to another file into the allTexts directory.
Writes Man of Law's tale to test file. Writes Wife of Bath's tale to validation file. All other tales are written to training file (all in data folder).

dict_formatter.py
Cleans Chaucer glossary (https://www.english.cam.ac.uk/converse/chaucer/glossary.doc) for use as a baseline dictionary. Cleaned file is written to chaucer.dict in the data directory.
