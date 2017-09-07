import urllib
import csv
import pandas as pd
import os

# default='warn' to get rid of SettingWithCopyWarning
pd.options.mode.chained_assignment = None  

#set variables
infile = #'path to CSV input file'
outfile = #'path to CSV output file'

# Create a new dataframe from a csv file
df = pd.read_csv(infile)

#URLs from dataframe to list
urls = df['URL'].tolist()

#create empty list
urlStatus = []

print ("checking urls......")

#loop to get url status
for i in urls:
	code = urllib.urlopen(i).getcode()
	urlStatus.append(code)

#list to series
se = pd.Series(urlStatus)

#series to column
df['URL Status'] = se.values

#remove output file if exists
try:
	os.remove(outfile)
except OSError:
	pass

#save
df.to_csv(outfile, index=False)

# done
print("done")