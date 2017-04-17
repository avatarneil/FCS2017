import numpy as np
import csv 

scaler = 3
i=0
j=0
j=j+scaler
k=0

data2006nonull = list(csv.reader(open("tempdata/post2006dataNoNull.csv")))
data2006nonull = np.array(data2006nonull)

data2006nonullsplit = []

ID = ''

templist = []

IDlist = []

IDcount=[]

templist = []

temp = ''
bigtemparray=[[]]
while (i<data2006nonull.size):
    data2006nonullsplit.append(str(data2006nonull[i]))
    i+=1
i=0

print('done pt1')
print(data2006nonull.size)
while (i<data2006nonull.size):
    idchecker=True
    while (j <= 10+scaler):
        ID = ID + data2006nonullsplit[i][j]
        j+=1
    j=19 + scaler
    while (j <= 22+scaler):
        if (j==19+scaler and data2006nonullsplit[i][j] == '-'):
            temp=temp+data2006nonullsplit[i][j]
        elif (data2006nonullsplit[i][j]=='0'or data2006nonullsplit[i][j]=='1' or data2006nonullsplit[i][j]=='2' or data2006nonullsplit[i][j]=='3' or data2006nonullsplit[i][j]=='4' or data2006nonullsplit[i][j]=='5' or data2006nonullsplit[i][j]=='6' or data2006nonullsplit[i][j]=='7' or data2006nonullsplit[i][j]=='8' or data2006nonullsplit[i][j]=='9'):
            temp = temp + data2006nonullsplit[i][j]
        j+=1
    k=0
    while (k <= len(IDlist)):
        if (len(IDlist)==0):
            IDlist.append(ID)
            idindex=0
            templist.append(temp)
        if (IDlist[k-1] == ID):
            idchecker=False
            idindex=k-1
            if (temp[0] == '-' and templist[idindex][0] == '-'):
                templist[idindex] = [-1*int(templist[idindex][1:]) + (-1*int(temp[1:]))]
            elif (temp[0] == '-'):
                templist[idindex] = [int(templist[idindex][0]) + (-1*int(temp[1:]))]
            elif(templist[idindex][0] == '-'):
                templist[idindex] = [-1*int(templist[idindex][1:]) + int(temp)]
            else:
                print(temp,templist[idindex][0],i,ID)
                templist[idindex] = [int(templist[idindex][0]) + int(temp)]
        k+=1
    k=0
    if (idchecker==True):
        IDlist.append(ID)
        idindex=len(IDlist)-1
        templist.append(temp)
    temp = ''
    j=0 + scaler
    ID = ''
    i+=1
i=0
print(IDlist)