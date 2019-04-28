import re
import time
def tokenize(content):

    source_code = content.split()
    source_code_index = 0

    tokens = []
    found_for = 0
    while source_code_index < len(source_code):
        word = source_code[source_code_index]

        """extract the code inside the for and store it
        Can be done via dictionaries as well"""
        if found_for == 1:
            if word == "}":
                found_for = 0
            elif word =="{":
                pass
            else:
                tokens.append(["FOR_STATEMENT",word])

        """extract the for loop statement and store it in a list  """       
        if "for" in word:
            tokens.append(["FOR_LOOP",word])
            found_for = 1

        source_code_index+=1

    parse(tokens)

def parse(tokens):

    statement_list = []

    for token in tokens:
         #extract the count 
        if token[0] == "FOR_LOOP":
            answer = token[1].split(";")
            count = re.split('<|>|=|<=|>=',answer[1])[1]

        #extract the statement
        if token[0] == "FOR_STATEMENT":
            statement_list.append(token[1])

    eliminate(statement_list,count)


"""function eliminate removes the for loop"""
def eliminate(statement_list,count):
    with open('test.c','r') as file:
        lines = file.readlines()

    line_no = 0
    for line in lines:   
        if "for" in line:
            for j in range(int(count)):
                """writes statements as they are in statement list"""
                for statements in statement_list:
                    lines[line_no] = statements+"\n"
                    line_no+=1
                    last_line_no = line_no
                j=j+1
        line_no+=1
      
    lines[last_line_no+1] = "}"

    with open('code_opt.c','w') as file:
        file.writelines(lines)

def main():
    print("Unrolling all loops.....\nPlease wait")
    time.sleep(5)
    print("Unroll completed")

    with open("test.c","r") as file:
        lines = file.read()
    tokenize(lines)


main()