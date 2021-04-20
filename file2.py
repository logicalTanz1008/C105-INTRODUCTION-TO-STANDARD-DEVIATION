import statistics
import csv
import pandas as pd

file = pd.read_csv('data.csv')
fileList = file.tolist()

sd = statistics.stdev(fileList)
print('Standard Deviation: ', sd)