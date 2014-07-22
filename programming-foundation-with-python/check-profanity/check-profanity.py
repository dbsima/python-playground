import os, urllib

def read_text():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = current_dir + "/movie_quotes.txt"
    
    quotes = open(path)
    contents_of_file = quotes.read()
    quotes.close()
    print contents_of_file
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen('http://www.wdyl.com/profanity?q='+text_to_check)
    output = connection.read()
    connection.close()
    if 'true' in output:
        print 'Profanity alert!'
    elif 'false' in output:
        print 'This document has no curse words!'
    else:
        print 'Could not scan the document properly.'
    
read_text()