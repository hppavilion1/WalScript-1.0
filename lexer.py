def encode(s):
    return s.replace('\\n', '\n').replace('\\t', '\t')

def lex(script):
    r=[]
    script=script.strip()
    script=script.split(';')[:-1]
    
    for x in range(len(script)):
        com=script[x].split('}')[:-1]
        
        for x in range(len(com))[1:]:
            if com[x][0]=='{':
                com[x]={'ARG':com[x],
                        'TYPE':'exp'}
            elif com[x][0]=='[':
                com[x]={'ARG':com[x],
                        'TYPE':'bool'}
            else:
                com[x]={'ARG':encode(com[x]),
                        'TYPE':'raw'}
                
        r.append({'COMMAND':com[0].strip(),
                  'ARGS':com[1:]})

    return r
        
