#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: October 27,2020
#this program displays the shelter population


import matplotlib.pyplot as plt
import pandas as pd

n=input('enter name of input file: ')
save=input('enter name of output file: ')

homeless=pd.read_csv(n)
homeless["Fraction Single Women"]=homeless["Single Adult Women in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x="Date of Census",y="Fraction Single Women")
fig=plt.gcf()
fig.savefig(save)
