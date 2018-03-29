import matplotlib.pyplot as plt
days = [1,2,3,4,5]
sleeping = [8,8,9,6,11]
eating = [2,3,2,2,1]
playing = [4,5,4,4,6]
working = [8,8,7,8,11]
plt.plot([],[],color="red",label="sleeping",linewidth=5)
plt.plot([],[],color="blue",label="eating",linewidth=5)
plt.plot([],[],color="black",label="playing",linewidth=5)
plt.plot([],[],color="pink",label="working",linewidth=5)

plt.stackplot(days,sleeping,eating,playing,working, colors=["red","blue","black","pink"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("stackplots")
plt.legend()
plt.show()
