import re
import csv
import pandas as pd

quest_file = open("Q.txt")
ans_file = open("A.txt")

quest=[]

for i in quest_file :
    i = re.sub('^\d*\.','',i)
    i = i.strip()
    quest.append(i)

ans=[]

for c in ans_file :
    c = re.sub('^\d*\:','',c)
    c = c.strip()
    ans.append(c)

page=['1']*45
link=['http://gstcouncil.gov.in/faq']*45
print(len(quest),len(ans),len(page),len(link))
data = {'question':quest,'answers':ans,'page':page,'link':link}

df =  pd.DataFrame(data)

export = df.to_csv('faq_data.csv')

'''
csvfile = csv.writer(open('txt2csv1','w'),delimiter=',',quoting=csv.QUOTE_ALL)
csvfile.writerow(p)
'''
