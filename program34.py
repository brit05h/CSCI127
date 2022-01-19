
#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: October 27,2020
#this program modifies the one from lab 7

import pandas as pd
import matplotlib.pyplot as plt

inp=input("enter name of input file: ")
out=input("enter name of output file: ")

df=pd.read_csv(inp)
df["Date"]=pd.to_datetime(df["Date"].apply(str))

df["% Attending"]=(df["Present"]/df["Enrolled"])*100

graph=df.plot(x="Date",y="% Attending")

fig=plt.gcf()
fig.savefig(out)
plt.show()
