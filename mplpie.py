import matplotlib.pyplot as plt

activities = ["sleeping","eating","playing","working"]
cols=["red","green","blue","pink"]
slices=[10,4,2,8]

plt.pie(slices,
        labels=activities,
        colors=cols,
        shadow="true",
        startangle=90,
        autopct='%2.2f%%',explode=(0,0,0.1,0))

#plt.xlabel("x")
#plt.ylabel("y")
plt.title("pie chart")
plt.legend()
plt.show()
