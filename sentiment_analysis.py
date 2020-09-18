import pandas as pd
import snownlp
import csv

cdsenti=pd.read_csv('D:/Project/dataset/new/cdnotwh.csv',encoding='utf-8')
host= cdsenti[cdsenti['review'].str.contains('小姐姐',na=False)]
no_host = cdsenti[~cdsenti['review'].str.contains('小姐姐',na=False)].dropna()

listhost=host['review'].tolist()
list_nohost=no_host['review'].tolist()

senti_list=[]
for row in listhost:
    senti=snownlp.SnowNLP(row)
    senti_list.append(senti.sentiments)

with open('d:/project/dataset/nlp/cdhostsenti.csv','w+',newline='') as myfile:
    write =csv.writer(myfile)
    write.writerows(map(lambda x: [x], senti_list))

senti_list_nohost=[]
for row in list_nohost:
    senti=snownlp.SnowNLP(row)
    senti_list_nohost.append(senti.sentiments)
with open('d:/project/dataset/nlp/cdnohostsenti.csv','w+',newline='') as myfile:
    write =csv.writer(myfile)
    write.writerows(map(lambda x: [x], senti_list_nohost))



