def createsock(env, *args):
    import socket
    return (socket(socket.AF_INET, socket.SOCK_STREAM), env)

def bindsock(env, *args):
    import socket
    env[args[0]].bind((args[1], args[2]))
    return(None, env)

def closesock(env, *args):
    import socket
    env[args[0]].close()
    return (None, env)

def socklisten(env, *args):
    import socket
    env[args[0]].listen(args[1])
    return (None, env)

def sockrecv(env, *args):
    import socket
    return (args[0].recv(args[1]), env)

def socksend(env, *args):
    import socket
    env[args[0]].sendall(''.join(args))
    return (None, env)

self._createsock = createsock
self._bindsock = bindsock
self._closesock = closesock
self._socklisten = socklisten
self._sockrecv = sockrecv
self._socksend = socksend
