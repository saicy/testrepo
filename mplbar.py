import matplotlib.pyplot as plt
x = [1,2,3,6]
y = [7,8,9,10]
x2 = [4,5,9,11]
y2 = [12,15,19,8]
plt.bar(x,y,label="Bar1",color="blue")
plt.bar(x2,y2,label="Bar2",color="red")
plt.title("Bardiag\nred and blue")
plt.legend()
plt.show()
