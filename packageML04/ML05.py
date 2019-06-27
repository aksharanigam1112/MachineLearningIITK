# 2. b) Load the csv using numpy through web

import numpy
import urllib.request

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataset = numpy.genfromtxt(web_path , delimiter=',')

#print(dataset)

for l in dataset:
    print(l)

print("\nShape of the data from the url : ",dataset.shape )