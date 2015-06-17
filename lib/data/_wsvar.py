def var(env, *args): #variables
    if args[1:]:
        env[args[0]]=''.join([str(x) for x in args[1:]]) #Accumulate args 2+ into name arg 1
    else:
        env[args[0]]=None
    return (None, env)

self._var = var
