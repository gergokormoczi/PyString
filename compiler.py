line_input = 1
line = 0
code = []
code_line = ""
val = ''
var_name= ''
val_to_write = ""
statement = False
length_of_code = len(code) 

#lists of variables and values
variables = []
vals =[]

#lists of functions and their names
func_names = [ ]
funcs = []

if_list = ("==" , "!=" ,"<" , ">")

keywords = ("for" ,"if" , "write", "func")

filename = input("txt name?: ")

        #WRITING CODE IN TERMINAL
#while code_line != "r":
#   code_line = input(  str(line_input) + " ")
#    line_input += 1
#    code.append(code_line)
#    length_of_code = len(code)

with open( filename + ".txt", "r", encoding='utf-8' )as f:
    for line in f.readlines():
        code_line = line.rstrip()
        code.append(code_line)
        length_of_code = len(code)
            
  
#make code to output
print("______________________________")
print("")

x = 0
#separate the code per every line
while x <  len(code):
    if type(code[x]) == str:
        separated_code = code[x].split()
    else:
        separated_code = code[x]
    
    #write var.változó ----> write "value of variable"
    #recignize variables and manipulate codeline   
    for i in range( len(separated_code) ):
        if i < len(separated_code) and  type( separated_code[i] ) == str and "var." in separated_code[i]:
            almost_var_name = separated_code[i]
            var_name = almost_var_name[4:]
            if var_name in variables:
                for l in range( len(variables) ):
                    if var_name == variables[l]:
                        #var.változó = új érték
                        #reassign values
                        if separated_code[ 1] == "=":
                            ( vals[l] ) = separated_code[2:]
                        #var.változó += plusz érték
                        #add to values
                        if separated_code[ 1] == "+=":
                            if type(separated_code[i]) == int:
                                ( vals[l] ) += int(separated_code[2])
                            else:
                                ( vals[l] ) += separated_code[2:]
                        #var.változó ++
                        #add one to int
                        if separated_code[ 1] == "++":
                            ( vals[l] ) += 1
                        #changr var... to values
                        if  type(vals[l]) == list and separated_code[i -1] != ";":
                            #list to string
                            value = ""
                            for ele in vals[l]:
                                value += str(ele)
                                value += " "
                            separated_code[i] = value[:-1]
                            value = ""
                        elif separated_code[i -1] != ";": 
                            separated_code[i] = vals[l]
                                
                            
                            #WORK ON THIS
        #  "and" in in one line
        #write szia ; write világ
        if i <= len(separated_code) and ";" == separated_code[i] and  separated_code[0] != "if" and  separated_code[0] != "for"and  separated_code[0] != "func":
            index_of_end = separated_code.index(";")
            index_of_end += 1  
            code.insert(x + 1 , separated_code[index_of_end:])
            separated_code[index_of_end -1:] = ""


        #length 
        #var greet = hello world ||| write var.greet length  ---> 9
        if i < len(separated_code) and "length" ==  separated_code[i]:
            length = len(separated_code[i - 1])         
            separated_code[i - 1] = length    
            separated_code.remove(separated_code[i] )
            separated_code.append("")

        #index 
        if i < len(separated_code) and type(separated_code[i]) == str and "["  == separated_code[i] and "]"  == separated_code[i + 2] and separated_code[0] != "for":
            to_index = separated_code[i - 1]
            index = int( separated_code[i + 1])
            separated_code[i - 1] = to_index[ index ]
            separated_code.remove(separated_code[i])
            separated_code.remove(separated_code[i + 1])
            separated_code.remove(separated_code[i + 2])
            for i in range(3):
                separated_code.append("")

            
    #recognize functions
    if i < len(separated_code) and  type(separated_code[i]) == str and "func." in separated_code[i]:
        almost_func_name = separated_code[i]
        func_name = almost_func_name[5:]
        if func_name in func_names:
            for l in range(len(func_names)):
                if func_name == func_names[l]:
                    #next line = function
                    code.insert(x + 1 , funcs[l])

            #functin' is not assigned          

    #store variables and their values
    #var változo = érték
    if  separated_code[0] == "var" and separated_code[2] == '=':
        name = separated_code[1]
        #var változo = input kérdés
        #input as value
        if "input" in separated_code[3] :
            question = ""
            for ele in separated_code[4:]:
                question += ele + " "
            val = input(question)
        else:
            val =  separated_code[3:]
        
        if "int" in separated_code[3]:
            for ele in separated_code[4]:
                value_for_int = ele
            vals.append( int( *value_for_int) )
        elif type(val) == list:
            value_for_list = ""
            for ele in val:
                value_for_list += ele + " "
            vals.append(value_for_list[:-1])
        else:
            vals.append(val)
        variables.append(name)

    #store functions
    #func funkction = do something /write hello world/
    if separated_code[0] == "func" and separated_code[2] == '=':
        function_name = separated_code[1] 
        in_function =  separated_code[3:]
        func_names.append(function_name)
        funcs.append(in_function)


        
            #automatically string   
    #write hello world
    #writing
    if separated_code[0] == "write":
        to_write = separated_code[1:] 
        print(*to_write)

    # for 10 write hello world    
    #for cycle
    if separated_code[0] == "for":
        for y in range(int(separated_code[1])):
            index_of_koto = separated_code.index("-")    
            index_of_koto += 1
            code.insert(x + 1, separated_code[index_of_koto:])
            
    #if 5 == 6 than write true else if 5 != 5 than write true else write false        
    #if statement
    if separated_code[0] == "if" and separated_code[4] == "than": 
        statement = False
        first = separated_code[1]
        statement = separated_code[2]
        second = separated_code[3]
        true_false = False
        if statement == ">":
            if first > second:
                true_false = True
        if statement == "<":
            if first < second:
                true_false = True
        if statement == "==":
            if first == second:
                true_false = True    
        if statement == "!=":
            if first != second:
                true_false = True
        if statement == "in":
            if first in second:
                true_false = True
        #true without else
        if true_false == True and "else" not in separated_code:
            index_of_than = separated_code.index("than")    
            index_of_than += 1
            code.insert(x + 1, separated_code[index_of_than:])

        #statement = false -> else
        if true_false == False and "else" in separated_code:
            index_of_else = separated_code.index("else")    
            index_of_else += 1
            code.insert(x + 1 , separated_code[index_of_else:])
        
        #statement = true -> ignore else
        if true_false == True and "else" in separated_code:
            index_of_else = separated_code.index("else")    
            code.insert(x + 1 , separated_code[0:index_of_else])
            
    x += 1
print("______________________________")