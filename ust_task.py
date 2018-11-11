import re

def frame(string_words):
    size = max(len(word) for word in string_words)
    print('*' * (size + 4))
    for word in string_words:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))

string=raw_input("Enter the input:")
exp=re.compile('^[a-zA-Z\s\.]+$')
if exp.match(string):
    string_words=string.split()
    frame(string_words)
else:
    print "Please enter string without special characters and numbers"