import matplotlib.pyplot as plt

plt.plot( [1,2,3,4] , [1,4,9,16] , 'bo-')      # b- means blue silid line
                                              # ro means red circle dot
plt.xlabel("Some Nos------>")
plt.ylabel("Squared values------>")
plt.axis([0,5,0,17])                # first 2 values rep the range of x-axis and the other 2 rep the range
                                    # of y axis
plt.show()

# character colour
# 'b' blue
# 'g' green
# 'r' red
# 'c' cyan
# 'm' magenta
# 'y' yellow
# 'k' black
# 'w' white

