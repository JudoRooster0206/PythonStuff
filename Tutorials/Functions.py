Var1 = 5
Var2 = 115

def Add(x, y=3):
    """
    param x:int
    param y:int
    Returns sum of x + y
    """
    return x + y
def Globalization():
    global Var1
    global Var2
    return Var1 + Var2

if Add(10) >= 15:
    print("Bigger than 15")
else:
    print("Lower than 15")

print(Globalization())
