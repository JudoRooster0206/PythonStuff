#Challenge 1
"""
Returns a squared number
param x: int
return x^2
"""
def Squared(x):
    return x ** 2

print(Squared(5))

#Challenge 2
def StringFunc(str1):
    """
    Returns a printed string
    param str1: string
    return print(str1)
    """
    str(str1)
    return print(str1)

StringFunc("Logy")
#Challenge 3

def ThreeParams(Var1, Var2, Var3, Var4=7, Var5= 3):
    """
    Returns 3 parameters and 2 optional parameters.
    param Var1: int
    param Var2: int
    param Var3: int
    param Var4: int
    param Var5: int
    return Var1 + Var2 + Var3 + Var4 + Var5
    """
    return Var1 + Var2 + Var3 + Var4 + Var5

print(ThreeParams(5, 5, 5))
print(ThreeParams(5, 5, 5, 9, 7))


#Challenge 4
def Divide(x):
    """
    Returns x divided by 2
    param x: int
    return x/2
    """
    return x/2

def Multiply(x):
    """
    Returns x multiplied by 4
    param x: int
    return x*4
    """
    return x*4

Result= Divide(4)
print(Multiply(Result))

#Challenge 5
def Float_Convert(Str1):
    """
    Returns a string converted to a float.
    param Str1: string
    return None
    """
    try:
        float(Str1)
        print(Str1)
    except ValueError:
        print("Parameter must be a number")

Float_Convert("Hey")
Float_Convert("10")
