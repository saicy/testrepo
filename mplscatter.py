import matplotlib.pyplot as plt
x = [1,2,5,7,3,5,7,9]
y = [3,5,8,3,6,8,4,2]
plt.scatter(x,y,label="scatskit",color="red",marker="*",s=10)
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatter plots")
plt.show()
