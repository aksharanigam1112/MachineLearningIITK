import matplotlib.pyplot as plt
x = [2,3,4,5,6,7]
y = [4,9,16,25,36,49]

# Markerefacecolor means the color of the point, marker size is the size of the dot while color is of the line
plt.plot(x,y,marker='o',markerfacecolor='red',markersize=10,linestyle = 'dashed',color='blue')

plt.title("Number with squared values")
plt.xlabel("Numbers------>" , fontsize=14,color='red')
plt.ylabel("Square------>" , fontsize=14,color='blue')

plt.axis([1,8,3,50])
plt.grid(True)

# Remark about some specific point , text starts from the coordinate 3,40 and it points to 5,25, shrink function
# shrinks the arrow by 10%
# plt.annotate('Square of 5' , xytext=(3,40) , xy=(5,25) , arrowprops=dict(facecolor='black' , shrink=.1))

plt.show()