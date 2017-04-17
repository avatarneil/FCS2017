import numpy as np
import csv

scaler = 3

tempdata = list(csv.reader(open("tempdata/tempdata.csv")))
tempdata = np.array(tempdata)

tempmetadata = list(csv.reader(open("tempdata/tempmetadata.csv")))
tempmetadata = np.array(tempdata)
tempdatasplit = []

datestring = ''
dates = []

keepdata = []

output = []

i=0
j=11+scaler

failnum = 0
 #OBJECTIVE: OUTPUT ONLY PAST 10 YEARS OF DATA
#368360

#OFF BY 3

while (i<368360):
    tempdatasplit.append(str(tempdata[i]))
    i=i+1
i=0

print("done pt1")

while (i<368360):
    while (j<=14+scaler):
        datestring = datestring + tempdatasplit[i][j]
        j+=1
    if (datestring[3]=='T'):
        failnum+=1
    elif int(datestring) >= 2006:
        keepdata.append(tempdatasplit[i])
    datestring = ''
    j=11+scaler
    i+=1 #endofloop
i=0

with open('post2006data.csv', 'w') as file:
    write = csv.writer(file,delimiter = ' ')
    while (i<len(keepdata)):
        write.writerow(keepdata[i])
        i+=1
    i=0