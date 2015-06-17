def delete(env, *args):
    del env[args[0]]
    return (None, env)
