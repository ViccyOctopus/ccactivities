#5. Sales After Tax
#Calculate the sales tax included after you buy one product. The sales tax in 
#Florida is 6%. (Hint: Use 1.06 to multiply)

print("What is the original price of the product?")
oriPrice = input()
intPrice = int(oriPrice)

totTax = (intPrice*1.06)
endPrice1 = (totTax - intPrice)
endPrice2 = (endPrice1 + intPrice)
Price = str(endPrice2)

print("Your total price after taxes would be " + Price + ".")