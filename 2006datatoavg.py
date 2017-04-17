import numpy as np
import csv 

scaler = 3
i=0
j=0
j=j+scaler

data2006nonull = list(csv.reader(open("tempdata/post2006dataNoNull.csv")))
data2006nonull = np.array(data2006nonull)

data2006nonullsplit = []

ID = ''

IDtemplist = [[]]

IDcount=[]

temp = ''

while (i<data2006nonull.size):
    data2006nonullsplit.append(str(data2006nonull[i]))
    i+=1
i=0

print('done pt1')
print(data2006nonull.size)
while (i<data2006nonull.size):
    while (j <= 10):
        ID = ID + data2006nonullsplit[i][j]
        j+=1
    j=19
    while (j <= 23):
        temp = temp + data2006nonullsplit[i][j]
        j+=1
    j=0
    while (j <= len(IDtemplist)):
        if(len(IDtemplist) == 0):
            IDtemplist[j].append([ID,temp])
            IDcount[j].append(1)
        elif (ID == IDtemplist[j][0][0]):
            IDtemplist[j][1] = (IDtemplist[j][1] + temp)
            IDcount[j][1]+=1
        else:
            IDtemplist.append([ID,temp])
            IDcount.append([1])
        j+=1
    temp = ''
    j=0
    ID = ''
    print(i)
    i+=1
i=0
print(IDtemplist)