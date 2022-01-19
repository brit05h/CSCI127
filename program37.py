#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 2,2020
#this program asks the user for a CSV

import pandas as pd

Fname=input('enter file name: ')
filmPermits=pd.read_csv(Fname)

print('there were', len(filmPermits), 'fil permits.')

print(filmPermits["Borough"].value_counts())

print("the three most popular type of events were: ",filmPermits["EventType"].value_counts())
