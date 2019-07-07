import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings(action="ignore")

plt.figure(1)
plt.subplot(311)            # 3,1,1 means 3 rows , 1 cols , select block 1
plt.plot([1, 2, 3],'ro-')

plt.subplot(312)            # 3 rows , 1 cols , 2nd block
plt.plot([4, 5, 6],'co-')

plt.subplot(313)
plt.plot([7, 8, 9],'go-')

plt.figure(2)
plt.plot([11, 12, 13])      # if we don't use subplot by default it is 1,1,1

plt.figure(1)
plt.subplot(311)
plt.title('Easy as 1,2,3')

plt.show()
