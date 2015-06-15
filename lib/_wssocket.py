def createsocket(env, *args):
    import socket
    return (socket(socket.AF_INET, socket.SOCK_STREAM), env)

def bindsocket(env, *args):
    env[args[0]].bind((args[1], args[2]))
    return(None, env)

def socklisten(env, *args):
    env[args[0]].listen(args[1])
    return (None, env)

def sockrecv(env, *args):
    return args[0].recv(args[1])
