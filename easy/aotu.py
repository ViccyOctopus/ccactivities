#3. Access Only to You
#Write a program that asks for your name, and if you were to input your name,
#then the computer greets you in a friendly manner/recognizes you. If 
#you were to put in any other name, the computer rejects you and you do not have access.

name = input("What is your name? ")
if name == "Victoria":
    print("Great! Welcome back!")
else:
    print("Access Denied.")