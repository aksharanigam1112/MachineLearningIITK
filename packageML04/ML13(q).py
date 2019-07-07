import matplotlib.pyplot as plt

labels = 's1','s2','s3'

sec = [30,50,20]
col = ['c','g','y']

plt.pie(sec , labels=labels , colors = col , startangle=90 , explode=(0,0.1,0) , autopct='%20.2f%%')

# Explode is used to separate the sections by the %age give like (0,0.1,0) means it will separate the 2nd section by 10%
# Startangle is used to define the starting angle from where the drawing has to start
# autopct print the float value in every piece, round off to 2 position & have 20 places

#plt.axis('Equal')
plt.title('Pie chart Example')
plt.show()
