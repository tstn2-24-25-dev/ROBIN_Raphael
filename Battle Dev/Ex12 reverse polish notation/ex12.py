def main():
    path = "input.txt"
    rpn = formatString(readfile(path))
    string = ""
    for x in rpn: 
        string += str(x)+" "
    print(f"{string} = {compute(rpn)}")

operators = ['+','-','*','/']

def readfile(path:str) -> str:
    with open(path) as file:
        content = file.readline()
        return content

def formatString(content:str)-> list:
    rpn = content.strip().split(' ')
    for x in range(len(rpn)):
        n=rpn[x]
        if n not in operators:
            rpn[x] = int(n)
    return rpn

def compute(rpnlist:list)->int:
    return rpn(rpnlist)[0]

def rpn(rpnlist:list,index:int=0) -> tuple[list,int]:
    if type(rpnlist[index]) == int:
        return rpnlist[index],index
    
    elif rpnlist[index]=='+':
        left,index = rpn(rpnlist,index+1)
        right,index = rpn(rpnlist,index+1)
        return left + right,index

    elif rpnlist[index]=='-':
        left,index = rpn(rpnlist,index+1)
        right,index = rpn(rpnlist,index+1)
        return left - right,index
    elif rpnlist[index]=='*':
        left,index = rpn(rpnlist,index+1)
        right,index = rpn(rpnlist,index+1)
        return left * right,index
    elif rpnlist[index]=='/':
        left,index = rpn(rpnlist,index+1)
        right,index = rpn(rpnlist,index+1)
        return left / right,index

if __name__=="__main__":
    main()