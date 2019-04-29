import re
"""split all text into tokens"""
def tokenize(contents):
    source_code = contents.split()
    source_code_index = 0
    tokens = []

    while(source_code_index < len(source_code)):
        word = source_code[source_code_index]
        source_code_index+=1
        tokens.append(word.split("="))

    remove_dead_code(tokens)

"""remove repeating subexpressions"""
def remove_dead_code(code_list):

    replace_dict = dict()
    for rhs in code_list:
        value = rhs[1]
        count = 0
        for values in code_list:
            if values[1] == value:
                count+=1
            if count > 1:
                code_list.remove(values)
                replace_dict[values[0]] = rhs[0]
                break
    
    replace_sub_expression(code_list,replace_dict)

"""replace the repeating expression with its first occurence"""
def replace_sub_expression(opt_code_list,replace_dict):
    for codes in opt_code_list:
        for key,values in replace_dict.items():
            if key in codes[1]:
                if "+" in codes[1]:
                    wow = codes[1].split("+")
                    wow[0] = values
                    wow = wow[0] + "+" +wow[1]
                    codes[1] = wow
                if "*" in codes[1]:
                    wow = codes[1].split("*")
                    wow[0] = values
                    wow = wow[0] + "*" +wow[1]
                    codes[1] = wow

    write_to_file(opt_code_list)

"""write to the file"""
def write_to_file(text):
    print(text)

    # cursor = 0
    # lines = []
    # for line in text:
    #     lines[cursor] = str(line) +'\n'
    #     cursor+=1

    with open('output.txt','w') as file:
        for line in text:
            file.write(str(line[0])+"="+str(line[1])+"\n")

def main():
    with open("cse.txt","r") as file:
        lines = file.read()

    tokenize(lines)

main()