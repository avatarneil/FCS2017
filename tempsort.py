import numpy as np
import csv

tempdata = list(csv.reader(open("tempdata/tempdata.csv")))
tempdata = np.array(tempdata)

tempmetadata = list(csv.reader(open("tempdata/tempmetadata.csv")))
tempmetadata = np.array(tempdata)