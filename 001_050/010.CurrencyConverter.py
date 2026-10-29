# This program show how many dollars you can buy with your money.

money = float(input("how much money do you have? R$ : "))

dollars = int(money / 5.25)
change = money - (dollars * 5.25)
missing = 5.25 - change

print(" You can buy",dollars,"dollars.") 

if money >= 5.25:
    print(" You can buy", "dollars.")
else:
    print("You need R$", missing,"more.") 



