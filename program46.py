
#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 16,2020
#this program asks the user for a number and prints out the corresponding month

def monthString(monthNum):
    monthString=""
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    monthString=months[monthNum -1]

    return(monthString)

def main():
    n=int(input("Enter the number of the month: "))
    while n<=0 or n>12:
        n=int(input("That is not a valid month number.Please enter a number between 1 and 12: "))
    nString=monthString(n)
    print("The month is", nString)

if __name__== "__main__":
    main()
        
