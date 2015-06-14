from __future__ import print_function
import os.path #For isfile
import sys
import lexer
from stack import *

def lexexp(s):
    s=s[1:]
    return s.split()

def evalarg(exp, env):
    if exp['TYPE'] == 'exp': #Float expression arguments
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

    elif exp['TYPE'] == 'str': #String expression arguments
        s=strstack(None)
        exp = lexexp(exp['ARG'])
        
        for x in range(len(exp)):
            for y in env:
                exp[x]=exp[x].replace('#'+y+'#', env[y]) #Swap out variables
        return ' '.join(exp)

    elif exp['TYPE'] == 'raw': #Raw expression Arguments
        return exp['ARG']
            
    
def evalargs(args, env):
    r=[]
    for x in args:
        r.append(evalarg(x, env))
    return r

class functionconstruct: #Basic functions. Not if-then constructs or anything.
    def _import(self, env, *args): #Import a module
        if os.path.isfile(args[0]):
            if args[0].endswith('.wal'):
                env=run(open(args[0]).read(), env)
                return True
            elif args[0].endswith('.py'):
                exec(open(args[0]).read()) #Build new functions from a file
                return True
            
            else:
                return False

    def _print(self, env, *args): #print command
        print(''.join([str(x) for x in args]), end='') #Accumulate args then print

    def _var(self, env, *args): #variables
        if args[1:]:
            env[args[0]]=''.join([str(x) for x in args[1:]]) #Accumulate args 2+ into name arg 1
        else:
            env[args[0]]=None

    def _input(self, env, *args): #Get user input
        return raw_input()

    def _skip(self, env, *args): #donothing
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

        elif c == '':
            pass
        
        else:
            raise ValueError('Invalid Command '+c)

        if v:
            env[v]=o
        i+=1

    return env

if __name__ == '__main__':
    run(open(sys.argv[1]).read())
