import matplotlib.pyplot as plt
"""
plt.plot([1,2,3],[5,7,4])
plt.show()
"""
x= [1,2,3]
y= [4,5,6]
x2= [1,2,3]
y2= [10,15,8]

plt.plot(x,y,label="first")
plt.plot(x2,y2,label="second")
plt.xlabel("time")
plt.ylabel("growth")
plt.title("growthtime\nsubtitle")
plt.legend()
plt.show()
