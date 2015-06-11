import lexer, args
from stack import *

def lexexp(s):
    return s.split()

def evalarg(exp):
    s = stack()
    if exp[1] == 'exp':
        exp = lexexp(exp)
        for x in exp:
            if x == '+':
                s.add()
            elif x == '-':
                s.sub()
            elif x == '*':
                s.mult()
            elif x == '/':
                s.div()
            else:
                try:
                    s.push(float(x))
                except:
                    pass
            
    elif exp[1] == 'raw':
        return exp
            
    
def evalargs(args):
    r=[]
    for x in args:
        r.append(evalarg(x))
    return r

def run(script, env={}):
    script = lex.lex(script)

    c=script['COMMAND']
    args=args.evalargs(script['ARGS'])
    
