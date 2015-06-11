def lex(script):
    r=[]
    script=script.strip()
    script=script.split(';')[:-1]
    
    for x in range(len(script)):
        com=script[x].split('}')[:-1]
        
        for x in range(len(com))[1:]:
            if com[x][0]=='{':
                com[x]={'ARG':com[x], 'TYPE':'exp'}
            else:
                com[x]={'ARG':com[x], 'TYPE':'raw'}
        r.append({'COMMAND':com[0],'ARGS':com[1:]})

    return r
        
