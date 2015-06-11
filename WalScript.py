from __future__ import print_function
import sys
import lexer
from stack import *

def lexexp(s):
    s=s[1:]
    return s.split()

def evalarg(exp, env):
    if exp['TYPE'] == 'exp':
        s = expstack()
        exp = lexexp(exp['ARG'])

        for x in exp:
            for y in env:
                x=x.replace('#'+y+'#', env[y]) #Swap out variables
            
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

        return s[-1]

    elif exp['TYPE'] == 'str':
        s=strstack()
        exp = lexexp(exp['ARG'])
        
        for x in range(len(exp)):
            for y in env:
                exp[x]=exp[x].replace('#'+y+'#', env[y]) #Swap out variables
        return ' '.join(exp)

    elif exp['TYPE'] == 'raw':
        return exp['ARG']
            
    
def evalargs(args, env):
    r=[]
    for x in args:
        r.append(evalarg(x, env))
    return r

def run(script, env={}):
    script = lexer.lex(script)
    i=0

    c=''

    while c != 'return':
        c=script[i]['COMMAND']
        args=evalargs(script[i]['ARGS'], env)

        if c == 'import':
            env=run(open(args[0]).read(), env)

        elif c == 'print':
            print(''.join([str(x) for x in args]), end='') #Accumulate args then print

        elif c == 'var':
            if args[1:]:
                env[args[0]]=''.join([str(x) for x in args[1:]]) #Accumulate args 2+ into name arg 1
            else:
                env[args[0]]=None

        elif c == 'input':
            env[args[0]] = raw_input() #Get raw input

        elif c == 'skip':
            pass
            
        i+=1

    return env

if __name__ == '__main__':
    run(open(sys.argv[1]).read())
