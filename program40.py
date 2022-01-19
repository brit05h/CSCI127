#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 2,2020
#this program writes a decision-making program

def computeScore(answers):
    housingscore = 0

    #Inp1
    if answers[0] == 1:
       housingscore = housingscore + 1
    elif answers[0] == 2:
       housingscore = housingscore + 2 
    elif answers[0] == 3:
       housingscore = housingscore + 3
    elif answers[0] == 4:
       housingscore = housingscore + 4
    else:
       housingscore = housingscore
    #2       
    if answers[1] >= 23:
       housingscore = housingscore + 1
    else:
       housingscore = housingscore
    #3      
    if answers[2] == "Yes":
       housingscore = housingscore - 1
    else:
       housingscore = housingscore
    #4      
    if answers[3] == 1:
       housingscore = housingscore + 1
    else:
       housingscore = housingscore
    #5      
    if answers[4] >= 3.5:
       housingscore = housingscore + 1
    else:
       housingscore = housingscore
    return(housingscore)

def main():
    print('Question 1')
    inp1 = int(input('What year are you?(1,2,3,4)'))
    print('Question 2')
    inp2 = int(input('How old are you?'))
    print('Question 3')
    inp3 = str(input('Are you currently on probation? (Yes or No)'))
    print('Question 4')
    inp4 = int(input('Are you Part-time or Full-time? (0 or 1)'))
    print('Question 5')
    inp5 = float(input('What is your GPA?'))
    answers = [inp1,inp2,inp3,inp4,inp5]
    housingscore = computeScore(answers)

    print("your housing score is", housingscore)
    
if __name__ == "__main__":
     main()
