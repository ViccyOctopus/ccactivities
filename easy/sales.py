#Prompt: Sales Prediction
#A company has determined that its annual profit is typically 23 percent of total sales. Write
#a program that asks the user to enter the projected amount of total sales, and then displays
#the profit that will be made from that amount.
#Hint: Use the value 0.23 to represent 23 percent.

annuprofit = input("Input the annual profit: ")
intprofit = int(annuprofit)
profit = intprofit*0.23
str_profit = str(profit)
print("Your total amount of profit is " + str_profit)