
import csv


with open('names.csv','a') as nf:
	x=csv.writer(nf)
	x.writerow(['h','c','60'])
	x.writerow(['h1','c1','6'])
