#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import numpy as np
a=np.zeros(shape=(10,14))
b=np.zeros(shape=(10,14))
N=15;
for k in range(10):
    num=str(k)
    dec='.\productDownload_2021-10-18T182724\ACSDT5Y201'+num+'.B01001D_data_with_overlays_2021-10-18T182652.csv'
    with open(dec, 'r') as f:  
        reader = csv.reader(f)
        result = list(reader)
        name=result[N][1]
        male_total=int(result[N][4])
        female_total=int(result[N][34])
        for i in range(14):
            j=(i+3)*2
            a[k][i]=int(result[N][j])/male_total
        for i in range(14):
            j=(i+18)*2
            b[k][i]=int(result[N][j])/female_total

y=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
clas=['Under 5 years','5 to 9 years','10 to 14 years','15 to 17 years','18 and 19 years','20 to 24 years','25 to 29 years','30 to 34 years','35 to 44 years','45 to 54 years','55 to 64 years','65 to 74 years','75 to 84 years','85 years and over']
for q in range(14):
    l1=plt.plot(y,a[:,q],'b--',label='male')
    l2=plt.plot(y,b[:,q],'r--',label='female')
    plt.plot(y,a[:,q],'bo-',y,b[:,q],'ro-')
    plt.title(name+'('+clas[q]+')')
    plt.xlabel('year')
    plt.ylabel('percentage')
    plt.legend()
    plt.savefig(name+'('+clas[q]+')'+".png")

