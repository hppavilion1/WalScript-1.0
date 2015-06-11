from __future__ import print_function
import lexer
from stack import *

def lexexp(s):
    return s.split()

def evalarg(exp, env={}):
    s = stack()
    if exp['TYPE'] == 'exp':
        exp = lexexp(exp)['ARG']
        for x in env:
            exp=exp.replace('#'+x+'#', env[x])
            
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
            
    elif exp['TYPE'] == 'raw':
        return exp['ARG']
            
    
def evalargs(args):
    r=[]
    for x in args:
        r.append(evalarg(x))
    return r

def run(script, env={}):
    script = lexer.lex(script)
    i=0

    c=''

    while c != 'RETURN':
        c=script[i]['COMMAND']
        args=evalargs(script[i]['ARGS'], env)
        
        if c == 'print':
            print(''.join(args), end='')

        elif c == 'var':
            env[args[0]]= ''.join(args[1:])

        i+=1
    

run('print}5};RETURN};')
