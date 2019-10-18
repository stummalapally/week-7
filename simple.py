import matplotlib.pyplot as plt
plt.figure(figsize=(5,15))
plt.plot([1,2,3,4],[1,4,9,16])
plt.title("First plot")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.xticks(fontsize=18)
#plt.xlabel("X Label",fontsize=20)
plt.xticks([1,2,3,4],["One","Two","Three","Four"])



plt.savefig("simple.png")
plt.show()

