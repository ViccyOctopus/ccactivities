# 1. Personal Information
#Write a program that displays the following information:
#• Your name
#• Your address, with the city, state, and ZIP
#• Your telephone number
#• Your college major


infopt1 = []
name = input("What is your name? (First and Last) ")
infopt1.append(name)

addy = []
addy1 = input("What city do you live in? ")
addy.append(addy1)
addy2 = input("What state do you live in? ")
addy.append(addy2)
addy3 = input("What is your ZIP? ")
addy.append(addy3)

infopt2 = []
num = input("What is your number?" )
infopt2.append(num)

cm = input("What is your college major? ")
infopt2.append(cm)

print(infopt1 + addy + infopt2)