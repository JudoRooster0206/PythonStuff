#Chapter 6
print("Challenge 1")
Cam="Camus"
for i in range(len(Cam)):
    print(Cam[i])

print("\nChallenge 2")
Str1=input("Enter a String:" )
Str2=input("Enter another:" )

result="Yesterday I wrote a {}. I sent it to {}!".format(Str1, Str2)
print(result)

print("\nChallenge 3")
Str1="aldous Huxley was born in 1984"
print(Str1.capitalize())

print("\nChallenge 4")
Str1= "Where now? Who now? When now?".split("?") #Supposed to get rid of question marks
print(Str1)

print("\nChallenge 5")
list=["The", "fox", "jumped", "over", "the", "fence", "."]
Str1=" ".join(list)
Str1= Str1[0: -2] + "."
print(Str1)

print("\nChallenge 6")
Str1="A screaming comes across the sky."
print(Str1.replace("s", "$"))

print("\nChallenge 7")
Str1="Hemingway"
print(Str1.index("m"))

print("\nChallenge 8")
print("'You are a flower'")

print("\nChallenge 9")
Str1="three "
print(Str1 + Str1 + Str1)
print(Str1 * 3)

print("\nChallenge 10")
Str1="It was a bright cold day in April, and the clocks were striking thirteen"
print(Str1[34:])
