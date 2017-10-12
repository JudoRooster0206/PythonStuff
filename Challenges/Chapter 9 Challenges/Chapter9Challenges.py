import os
import csv

print("\nChallenge 1:")
path=os.path.join("C:", "\\Users", "nicko", "OneDrive", "Documents", "SSH_Commands.txt")
with open(path, "r") as ReadFile:
    print(ReadFile.read())

print("\nChallenge 2:")
answer= input("What's your favorite color?: ")
with open("Color.txt", "w") as File:
    File.write(answer)

with open("Color.txt", "r") as File:
    print(File.read())
    
print("\nChallenge 3:")
with open("CSVfile.csv", "w", newline='') as File:
    Write = csv.writer(File, delimiter=",")
    Write.writerow(["Top Gun", "Risky Business", "Minority Report"])
    Write.writerow(["Titantic", "The Revenant", "Inception"])
    Write.writerow(["Training Day", "Man on Fire", "Flight"])

with open ("CSVfile.csv", "r") as File:
    Read = csv.reader(File, delimiter=",")
    for row in File:
        print(row)
