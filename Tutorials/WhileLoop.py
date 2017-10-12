times = input("How many times would you like to say \'Hello World\' ?: ")
times = int(times)
while times > 0:
    print("Hello World")
    times-=1

qs = ["What is your name?", "What is your fav. color?", "What is your quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
