from __future__ import print_function
import os.path #For isfile
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
        s=strstack(None)
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

class functionconstruct:
    def _import(self, env, *args):
        if isfile(args[0]):
            if args[0].endswith('.wal'):
                env=run(open(args[0]).read(), env)
                return True
            elif args[0].endswith('.py'):
                return True
            
            else:
                return False

    def _print(self, env, *args):
        print(''.join([str(x) for x in args]), end='') #Accumulate args then print

    def _var(self, env, *args):
        if args[1:]:
            env[args[0]]=''.join([str(x) for x in args[1:]]) #Accumulate args 2+ into name arg 1
        else:
            env[args[0]]=None

    def _input(self, env, *args):
        return raw_input() #Get raw input

    def _skip(self, env, *args):
        return None

evaluator = functionconstruct()

def run(script, env={}):
    script = lexer.lex(script)
    i=0
    c=None

    while c not in ['return', 'debug']:
        o=None
        v=script[i]['VAR']
        c=script[i]['COMMAND']
        args=evalargs(script[i]['ARGS'], env)

        if '_'+c in dir(evaluator):
            o=getattr(evaluator, '_'+c)(env, *args)
            
        elif c == 'return':
            pass
        
        else:
            raise ValueError('Invalid Command '+c)

        if v:
            env[v]=o
        i+=1

    return env

if __name__ == '__main__':
    run(open(sys.argv[1]).read())
