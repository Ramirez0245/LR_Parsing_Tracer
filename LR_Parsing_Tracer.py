"""
Given the following CFG and the LR Parsing table. A program to trace the input strings 
(1) (i+i)*i$       (2) (i*)$.  

(1)	E-->E + T
(2)	E -->E – T
(3)	E --> T
(4)	T-->T * F
(5)	T--> T/F
(6)	T--> F
(7)	F-->( E )
(8)	F--> i	
FIRST( E ) ={    (  i       }
FIRST (T ) = {   (  i       }
FIRST( F ) = {   (   i      }	
FOLLOW( E ) = {   $  + - )        }
FOLLOW( T ) = {   $ +  - ) * /   }
FOLLOW( F ) = {   $ +  - ) * /   }

"""
def main():
    word1 = "(i+i)*i$"
    word2 = "(i*)$"

    word = word1

    stack = []
    stack.append('0')
    state = stack.pop()

    read = word[0]
    word = word[1:]
    current_read = ""
    conditon = False
    count = 0
    while 1:
        count += 1
        if count == 100: break
        print("I'm running")
        print(stack)
        match state:
            case "0":
                if read == "i" :
                    stack.append("0")
                    stack.append("i")
                    stack.append("5")
                elif read == "(":
                    stack.append("0")
                    stack.append("(")
                    stack.append("4")
                elif read == "E":
                    stack.append("0")
                    stack.append("E")
                    stack.append("1")
                    read = current_read

                elif read == "T":
                    stack.append("0")
                    stack.append("T")
                    stack.append("2")
                    read = current_read
                elif read == "F":
                    stack.append("0")
                    stack.append("F")
                    stack.append("3")
                    read = current_read                                    
                else: 
                    break

            case "1":
                if read == "+":
                    stack.append("1")
                    stack.append("+")
                    stack.append("6")
                elif read == "-":
                    stack.append("1")
                    stack.append("-")
                    stack.append("7")
                elif read == "$":
                    conditon = True
                    break
                else: 
                    break

            case "2": #R3 E->T
                if read == '+' or read == "-" or read == ")" or read == "$": 
                    stack.append("2")
                    stack.pop()
                    stack.pop()
                    current_read = read
                    read = "E"
                elif read == "*":
                    stack.append("2")
                    stack.append("*")
                    stack.append("8")
                elif read == "/":
                    stack.append("2")
                    stack.append("/")
                    stack.append("9")                
                else: 
                    break
            case "3":#R6 T->F
                if read == '+' or read == "*" or read == "/" or read == "-" or read == ")" or read == "$": #R3 E->T
                    stack.append("3")
                    stack.pop()
                    stack.pop()
                    current_read = read
                    read = "E"
                else: 
                    break
            case "4":
                if read == 'i':
                    stack.append('4')
                    stack.append('i')
                    stack.append('5')
                elif read == '(':
                    stack.append('4')
                    stack.append('(')
                    stack.append('4')
                elif read == 'E':
                    stack.append('4')
                    stack.append('E')
                    stack.append('10')
                    read = current_read                    
                elif read == 'T':
                    stack.append('4')
                    stack.append('T')
                    stack.append('2')  
                    read = current_read                    
                elif read == 'F':
                    stack.append('4')
                    stack.append('F')
                    stack.append('3')    
                    read = current_read                                                      
                else: 
                    break
            case "5": #F=>i
                if read == '+' or read == "-" or read == "*" or read == "/" or read == ")" or read == "$":
                    stack.append('5')
                    stack.pop()
                    stack.pop()
                    current_read = read
                    read = "F"
                else: 
                    break
            case "6": #F=>i
                if read == 'i':
                    stack.append('6')
                    stack.append('i')
                    stack.append('5')   
                elif read == ')':
                    stack.append('6')
                    stack.append(')')
                    stack.append('4')
                elif read == "F":
                    stack.append("6")
                    stack.append("F")
                    stack.append("3")
                    read = current_read 
                elif read == "T":
                    stack.append("6")
                    stack.append("T")          
                    stack.append("11")
                    read = current_read 
                else: 
                    break      
            case "7": 
                if read == 'i':
                    stack.append('7')
                    stack.append('i')
                    stack.append('5')
                elif read == '(':
                    stack.append('7')
                    stack.append('(')
                    stack.append('4')              
                elif read == "T":
                    stack.append("7")
                    stack.append("T")
                    stack.append("12")
                    read = current_read 
                elif read == "F":
                    stack.append("7")
                    stack.append("F")
                    stack.append("3")
                    read = current_read 
            case "8":
                if read == "i":
                    stack.append("8")
                    stack.append("i")
                    stack.append("5")
                elif read == "(":
                    stack.append("8")
                    stack.append("(")
                    stack.append("4")         
                elif read == "F":
                    stack.append("8")
                    stack.append("F")
                    stack.append("13")
                    read = current_read
            case "9":
                if read == "i":
                    stack.append("9")
                    stack.append("i")
                    stack.append("5")     
                elif read == "(":
                    stack.append("9")
                    stack.append("(")
                    stack.append("4")        
                elif read == "F":
                    stack.append("9")
                    stack.append("F")
                    stack.append("14")
                    read = current_read      
            case "10" :
                if read == "+":
                    stack.append("10")
                    stack.append("+")
                    stack.append("6")
                elif read == "-":
                    stack.append("10")
                    stack.append("-")
                    stack.append("7")          
                elif read == ")":
                    stack.append("10")
                    stack.append(")")
                    stack.append("15")  
                else:
                    break 
            case "11": #R1 E->E+T
                if read == "+" or read== "-" or read == ")" or read == "$":
                    stack.append("11") 
                    stack.pop()
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()        
                    current_read = read
                    read = "E"   
                elif read == "*":                    
                    stack.append("11")
                    stack.append("*")
                    stack.append("8")
                elif read == "/":                    
                    stack.append("11")
                    stack.append("/")
                    stack.append("9")    
                else: 
                    break
            case "12":  #R2 E=>E-T    
                if read == "+" or read== "-" or read == ")" or read == "$":
                    stack.append("12") 
                    stack.pop()
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()        
                    current_read = read
                    read = "E"   
                elif read == "*":                    
                    stack.append("12")
                    stack.append("*")
                    stack.append("8")
                elif read == "/":                    
                    stack.append("12")
                    stack.append("/")
                    stack.append("9")    
                else: 
                    break
            case "13": #R4 T->T*F
                if read == "+" or read== "-" or read == ")" or read == "$" or read == "*" or read == "/":
                    stack.append("13") 
                    stack.pop()
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()        
                    current_read = read
                    read = "T"  
                else:  
                    break
            case "14": #R5 T->T/F
                if read == "+" or read== "-" or read == ")" or read == "$" or read == "*" or read == "/":
                    stack.append("14") 
                    stack.pop()
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()        
                    current_read = read
                    read = "T"  
                else:  
                    break
            case "15": #R7 T->(E)
                if read == "+" or read== "-" or read == ")" or read == "$" or read == "*" or read == "/":
                    stack.append("15") 
                    stack.pop()
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()  
                    stack.pop()        
                    current_read = read
                    read = "T"  
                else:  
                    break 
        state = stack.pop()   
        print("Current stack len")
        size = len(stack)
        print(size)
        print("Current state") 
        print(state)  
        print("current stack")
        print(stack)
        print("current read")
        print(read)
        print("current word")
        print(word)
        if stack[size - 1] == read:
            stack.pop()
            read = word[0]
            word = word[1:]         



    if conditon:
        print("Word accepted!")
    else:
        print("Word not accepted")

# __name__ special variables
if __name__ == '__main__':
    main()