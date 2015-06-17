import sys, argparse
import WalScript

parser = argparse.ArgumentParser(prog='WalScript Interpreter')

parser.add_argument('file',                                                          help='The file to execute')
parser.add_argument('-i', '--interactive', action='store_true', dest='interactive',  help='Run REPL')
parser.add_argument('-c', '--compile',     action='store_true', dest='compile',      help='Compile the script to Python')
parser.add_argument('-o', '--output',      action='store',      dest='outfile',      help='Set the output file for compilation')
parser.add_argument('-v', '--version',     action='version', version='%(prog)s/0.7', help='Get the version')

args = parser.parse_args(sys.argv[1:])
args = vars(args)

if not args.get('compile'):
    WalScript.run(open(args['file']).read())
else:
    print('Compilation not yet supported')
    #WalScript.compile(open(args['file']).read(), out=args['output'])

if args.get('i'): #Repl
    env = {}
    while 1:
        env=WalScript.run(raw_input(), env)
