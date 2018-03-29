import matplotlib.pyplot as plt
pop_ages=[1,2,5,7,13,15,14,15,18,19,48,37,40,50,26,74,45,33,37]
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(pop_ages,bins,histtype='bar',rwidth=0.9)
plt.xlabel("x")
plt.ylabel("y")
plt.title("histogram")
plt.show()
