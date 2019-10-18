import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[elem * elem * elem for elem in x]

#plt.plot([1,2,3,4],[1,4,9,16],'go',x,y,"r^")
labels=["Squares","Cubes"]
plt.plot(x,[1,4,9,16],label=labels[0])
plt.plot(x,y,label=labels[1])
plt.legend()
plt.show()

