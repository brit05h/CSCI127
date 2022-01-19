#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 16,2020
#this program repeatedly asks the user for the price

print("------------------------------------------")
print("Welcome to the total with tax calculator!")
print("------------------------------------------")
print("Please enter the price of each item you would like to purchase, one at a time.")
print("Enter a negative number when you are done.")
print()
price=float(input("Enter the price of an item"))
total=0
while price > 0:
    total=total+price
    price=float(input("Enter the price of an item: "))
    n= total * 0.0875
    v=total+n

print("The total with tax is", v)
