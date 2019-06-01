import re

def tokenize(contents):

    tokens = []
    source_code = contents.split()
    keywords = ["print","if","else","return","def"]
    source_index = 0
    while source_index < len(source_code):
        word = source_code[source_index]

        if word == 'var':
            tokens.append(["VAR_DECLARATION",word])

        elif word in keywords:
            tokens.append(["KEYWORD",word])

        elif re.match('[a-zA-Z]',word):
            if word[len(word)-1] == ";":
                tokens.append(["IDENTIFIER",word[0:len(word)-1]])
            else:
                tokens.append(["IDENTIFIER",word])

        elif re.match('[0-9]',word):
            tokens.append(["INTEGER",word]) 
        
        elif word in "-/=*":
            tokens.append(["OPERATOR",word])

        source_index += 1
    print(tokens)

def main():
    with open('test.txt','r') as file:
        contents = file.read()
        tokenize(contents)
        
main()