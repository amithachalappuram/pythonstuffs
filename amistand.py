import csv
import time

search_string = "linkedin.com"

with open('/home/fullcontact-316/Desktop/amithamerge/11.csv','r') as f:
	reader = csv.DictReader(f)
	for row in reader:
      	if row[c3] == search_string:
        	print "ok"
        else:
        	print "wrong"
           