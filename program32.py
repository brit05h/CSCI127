
#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: October 27,2020
#this program explores another data set

import matplotlib.pyplot as plt
import pandas as pd

n=input('enter name of input file: ')
save=input('enter name of output file: ')

star=pd.read_csv(n)
stat=star.groupby(['geo_entity_name']).mean()['data_valuemessage']
stat.plot.bar()

plt.gcf().subplots_adjust(bottom=0.5)

fig=plt.gcf()
fig.savefig(save)
