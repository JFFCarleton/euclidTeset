#eulcid()
#Finds the greatest common denominator between two ints, a and b
# Params:
#   a = 1st desired int 
#   b = 2nd desired int
#   r = remainder after mod operation a%b
# returns: 
#   if a%b = 0, IE b is the GCD: returns b
#   else, Recursively calls itself, using r as the new b param: returns eulcid(b,r)

def eulcid(a,b):
    r = a%b
    if(r == 0):
        return b
    else:
        return eulcid(b,r)

output = eulcid(18,81)
print(output)
