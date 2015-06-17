import re

class LexerError(Exception):
    pass

def encode(s): #Backslash substitutions
    return s.replace('\\n', '\n').replace('\\t', '\t')

def lex(script): #Lex script
    r=[] #Return value (becomes list of var/command/arg dicts)
    script=script.strip().split(';')[:-1] #Clean out cruft and divide script by semicolons
    
    for x in range(len(script)):
        if len(script[x].split('='))>1: #Extract var (from var=command};)
            var=script[x].split('=')[0].strip()
            script[x]=''.join(script[x].split('=')[1:])
        else:
            var=None #Null variable
        
        com=script[x].split('}')[:-1] #Split arguments
        
        for x in range(len(com))[1:]: #Iterate through arguments
            if com[x][0]=='{': #Expression-type arguments
                if com[x][1]=='e': #Float-type expressions
                    com[x]={'ARG':com[x],
                            'TYPE':'exp'}
                    
                elif com[x][1]=='b': #Boolean-type expressions
                    com[x]={'ARG':com[x],
                            'TYPE':'bool'}
                    
                elif com[x][1]=='s': #String-type expressions
                    com[x]={'ARG':com[x],
                            'TYPE':'str'}

                else:
                    raise LexerError('Invalid expression-type encountered')

            else: #Raw-type arguments
                com[x]={'ARG':encode(com[x]),
                        'TYPE':'raw'}
                
        r.append({'VAR':var, #Build command object
                  'COMMAND':com[0].strip(),
                  'ARGS':com[1:]})

    return r
        
