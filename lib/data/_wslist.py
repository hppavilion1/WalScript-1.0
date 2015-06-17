def lis(env, *args): #lists
    if args[1:]:
        env[args[0]]=[''.join([str(x) for x in args[1:]])] #Accumulate args 2+ into name arg 1
    else:
        env[args[0]]=[]
    return (None, env)

def getitem(env, *args):
    return (env[args[0]][args[1]], env) #Get item from list

self._list = lis
self._getitem = getitem
