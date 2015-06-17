import re

def encode(s):
    return s.replace('\\n', '\n').replace('\\t', '\t')

def lex(script):
    r=[]
    script=script.strip()
    script=script.split(';')[:-1]
    
    for x in range(len(script)):
        if len(script[x].split('='))>1:
            var=script[x].split('=')[0].strip()
            script[x]=''.join(script[x].split('=')[1:])
        else:
            var=None
        
        com=script[x].split('}')[:-1]
        
        for x in range(len(com))[1:]:
            if com[x][0]=='{':
                if com[x][1]=='e':
                    com[x]={'ARG':com[x],
                            'TYPE':'exp'}
                    
                elif com[x][1]=='b':
                    com[x]={'ARG':com[x],
                            'TYPE':'bool'}
                    
                elif com[x][1]=='s':
                    com[x]={'ARG':com[x],
                            'TYPE':'str'}

        else:
            com[x]={'ARG':encode(com[x]),
                    'TYPE':'raw'}
                
        r.append({'VAR':var,
                  'COMMAND':com[0].strip(),
                  'ARGS':com[1:]})

    return r
        
