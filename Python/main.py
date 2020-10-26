import sys

def evaluate(code, stack=[]):
    c_str  = ""
    in_str = 0

    for c in code:
        c = str(c)
        if(in_str > 0):
            c_str += c
        if(c == "("):
            in_str += 1
        elif(c == ")"):
            in_str -= 1
            if(in_str == 0):
                stack.append(c_str[0:-1])
        
        if(not(in_str > 0)):
            if(c == "~"):
                if(len(stack) > 1):
                    tmp1 = stack.pop()
                    tmp2 = stack.pop()
                    stack.append(tmp1)
                    stack.append(tmp2)
            elif(c == ":"):
                if(len(stack) > 0):
                    tmp1 = stack.pop()
                    stack.append(tmp1)
                    stack.append(tmp1)
            elif(c == "!"):
                if(len(stack) > 0):
                    tmp1 = stack.pop()
            elif(c == "*"):
                if(len(stack) > 1):
                    tmp1 = stack.pop()
                    tmp2 = stack.pop()
                    stack.append(tmp2 + tmp1)
            elif(c == "a"):
                if(len(stack) > 0):
                    tmp1 = stack.pop()
                    stack.append("(" + tmp1 + ")")
            elif(c == "^"):
                if(len(stack) > 0):
                    tmp1 = stack.pop()
                    evaluate(tmp1, stack)
            elif(c == "S"):
                if(len(stack) > 0):
                    tmp1 = stack.pop()
                    print(tmp1, end="")
    return(stack)

evaluate(open(sys.argv[1], "r").read())
