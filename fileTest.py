import os
 
def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            if file_.endswith(".htm"):
                filename = file_.split('.')[0] + "_original.txt"
                print(filename)
           # print( os.path.join(root, file_) )
 
if __name__ == '__main__':
    top = os.getcwd()
    pywalker(top)
#pywalker('/Users/abhisheksoni/Documents/CS 8803 - CC/ChaucerText/tales')
