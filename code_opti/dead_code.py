import re

# tokenize creates tokens of all lines in the code
def tokenize(contents):

    tokens = []
    source_code = contents.split()
    keywords = ["print","return","def"]
    source_index = 0
    while source_index < len(source_code):
        word = source_code[source_index]

        if word == 'var':
            tokens.append(["VAR_DECLARATION",word])
        
        elif word == 'if':
            tokens.append(["IF_Statement",word])

        elif word ==";":
            tokens.append(["END_STATEMENT",word[len(word)-1]])

        elif word in keywords:
            tokens.append(["KEYWORD",word])

        elif re.match('[a-zA-Z]',word):
            tokens.append(["IDENTIFIER",word])

        elif re.match('[0-9]',word):
            tokens.append(["INTEGER",word]) 
        
        elif word in "-/=*==":
            tokens.append(["OPERATOR",word])

        source_index += 1
    print(tokens)
    parse(tokens)

# Function identifies dead code
def parse(tokens):
    len_of_tokens = len(tokens)
    variable_dict = dict()

    no_of_lines = 0
    for i in range(len_of_tokens):

       #search for a variable declaration and store in a dictionary
        if tokens[i][0] == "VAR_DECLARATION":
            variable_dict[tokens[i+1][1]] = tokens[i+3][1]
   
        #search for an if statement and store its condition
        if tokens[i][0] == "IF_Statement":
            var_name = tokens[i+1][1]
            var_value = tokens[i+3][1]
            line_no = no_of_lines
        
        #count no of lines in a file .IMO this could be done in a better way
        if tokens[i][0] == "END_STATEMENT":
            no_of_lines+=1
        
    before_if_value = variable_dict[var_name]
    after_if_value = var_value

    if before_if_value!=after_if_value:
        print("WE have a dead code here",line_no,line_no+1)
    
    eliminate(line_no,line_no+1)
    
    
# This function removes all the lines specified in the arguments
def eliminate(from_line_no,to_line_no):
    with open('test.txt','r') as file:
        lines = file.readlines()

    lines[from_line_no] = ""
    lines[to_line_no] = ""

    with open('test.txt','w') as file:
        file.writelines(lines)


def main():
    with open('test.txt','r') as file:
        contents = file.read()
        tokenize(contents)

main()