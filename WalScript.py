import lexer, args
def run(script, env={}):
    script = lex.lex(script)

    c=script['COMMAND']
    args=args.evalargs(script['ARGS'])
    
