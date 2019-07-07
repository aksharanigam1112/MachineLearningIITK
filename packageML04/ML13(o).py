# Bar Plot
import matplotlib.pyplot as plt

x1 = [1,3,4,5,6,7,9]
y1 = [4,7,2,4,7,8,9]

x2 = [2,4,6,8,10]
y2 = [5,6,2,6,2]

plt.bar(x1,y1,label = "Blue Bar" , color='b')
plt.bar(x2,y2,label = "Red bar" , color = 'r')
plt.plot(x1,y1,'ko-')
plt.plot(x2,y2,'wo--')

plt.xlabel("Bar no")
plt.ylabel("Bar height")
plt.title("Bar chart example")
plt.legend()
plt.show()