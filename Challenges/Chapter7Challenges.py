print("Challenge 1:")

List=["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for i in List:
    print(i)

print("\nChallenge 2:")

for i in range(25, 51):
    print(i)

print("\nChallenge 3:")

IndexNum=0;
for i in List:
    print("Item: {} Index: {}".format(IndexNum, i))
    IndexNum+=1

print("\nChallenge 4:")
NumList=[1, 2, 3, 4, 5]
choice = "Y"
while choice=="Y":
    choice = input("Continue?: (Y/N) ")
    if choice=="N" :
        break
    elif choice=="Y":
        guess = input("Guess a number: ")
        if int(guess) in NumList:
            print("You're correct.")
        else:
            print("Incorrect")
    else:
        print("Invalid")

    print(NumList)

print("\nChallenge 5:")
FirstList=[8, 19, 148, 4]
SecondList=[9, 1, 33, 83]
ThirdList=[]

for index1 in FirstList:
    for index2 in SecondList:
        num = index1 * index2
        ThirdList.append(num)

print(ThirdList)
