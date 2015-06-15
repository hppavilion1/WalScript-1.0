def wsprint(env, *args): #print command
    print(''.join([str(x) for x in args]), end='') #Accumulate args then print
    return((None, env))

def wsinput(env, *args): #Get user input
    return((raw_input(), env))
    
self._print = wsprint
self._input = wsinput
