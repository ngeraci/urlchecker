import urllib
import csv
import pandas as pd
import os

def main(): 

	# default='warn' to get rid of SettingWithCopyWarning
	pd.options.mode.chained_assignment = None  

	#set file path variables
	infile = 'C:/Users/ngeraci/Documents/core/ContentDMCleanup/wrca_millennium_urls.csv'
	outfile = 'C:/Users/ngeraci/Documents/core/ContentDMCleanup/wrca_millennium_urls_status2.csv'

	# Create a new dataframe from a csv file
	df = pd.read_csv(infile)

	#URLs from dataframe to list
	urls = df['Test URL'].tolist()

	#create empty list
	urlStatus = []

	#loop to get url status
	for i in urls:
		print ("checking " + str(i))
		code = urllib.urlopen(i).getcode()
		urlStatus.append(code)

	#write list to series
	se = pd.Series(urlStatus)

	#write series to column
	df['URL Status'] = se.values

	#delete the output file if it already exists
	try:
		os.remove(outfile)
	except OSError:
		pass

	#save
	df.to_csv(outfile, index=False)

	# done
	print('done')

if __name__ == '__main__':
    main()