from stack import *

def lexexp(s):
    return s.split()

def evalexp(exp):
    s = stack()
    if exp[1] == 'exp':
        exp = lexexp(exp)
        for x in exp:
            if x == '+':
                s.add()
            elif x == '-':
                s.sub()
            elif x == '*':
                s.mul()
            elif x == '/':
                s.div()

            else:
                s.push(float(x))
            
    elif exp[1] == 'raw':
        return exp
            
    
def evalargs(args):
    for x in args:
        
