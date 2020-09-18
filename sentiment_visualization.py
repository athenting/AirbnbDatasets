from matplotlib import pyplot as plt
import pandas as pd

cd=pd.read_csv('d:/project/dataset/nlp/cdhostsenti.csv',header=None)
cd_wh=cd.iloc[:,0]

plt.hist(cd_wh,bins=100,width=0.5,color='cornflowerblue',alpha=0.5,range=(0,1))
plt.axvline(cd_wh.mean(), color='cornflowerblue', linestyle='dashed', linewidth=1, label='mentioned hosts:' + str(round(cd_wh.mean(),2)))
plt.grid(axis='y',alpha=0.75)
plt.xlabel('Review sentiments',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Chengdu Reviews Sentiments mentioned hosts',fontsize=15)
plt.legend(loc='upper center')
plt.show()
