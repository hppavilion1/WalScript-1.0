def sqrt(env, *args):
    import math
    return (math.sqrt(args[0]), env)

def sin(env, *args):
    import math
    return (math.sin(args[0]), env)

def cos(env, *args):
    import math
    return (math.cos(args[0]), env)

def tan(env, *args):
    import math
    return (math.tan(args[0]), env)

def asin(env, *args):
    import math
    return (math.asin(args[0]), env)

def acos(env, *args):
    import math
    return (math.acos(args[0]), env)

def atan(env, *args):
    import math
    return (math.atan(args[0]), env)

def log(env, *args):
    import math
    return (math.log(args[0], args[1]), env)

def degrees(env, *args):
    import math
    return (math.degrees(args[0]), env)

def radians(env, *args):
    import math
    return (math.radians(args[0]), env)


self._sqrt    = sqrt
self._sin     = sin
self._cos     = cos
self._tan     = tan
self._asin    = asin
self._acos    = acos
self._atan    = atan
self._log     = log
self._degrees = degrees
self._radians = radians
