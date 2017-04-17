import numpy as np
import csv 

scaler = 3
i=0
j=19+scaler

data2006 = list(csv.reader(open("tempdata/post2006data.csv")))
data2006 = np.array(data2006)

data2006split = []

tempoutput = ''

keepdata = []

failnum=0

while (i<data2006.size):
    data2006split.append(str(data2006[i]))
    i=i+1
i=0

while (i<data2006.size):
    while (j<=23+scaler):
        tempoutput = tempoutput + data2006split[i][j]
        j+=1
    if (tempoutput=='-9999'):
        failnum+=1
    else:
        keepdata.append(data2006split[i])
    tempoutput = ''
    j=19+scaler
    i+=1 #endofloop
i=0
j=19

print(failnum)
with open('post2006dataNoNull.csv', 'w') as file:
    write = csv.writer(file,delimiter = ' ')
    while (i<len(keepdata)):
        write.writerow(keepdata[i])
        i+=1
    i=0