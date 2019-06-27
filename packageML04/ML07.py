# using pandas reading live data
import pandas
import urllib.request

hnames = ['sepal-length','sepal-width','petal-length','petal-width','class']

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")

dataFrame = pandas.read_csv(web_path ,names = hnames)

print("shape = ", dataFrame.shape)

print("\n",dataFrame)

print("columns : ", dataFrame.columns)