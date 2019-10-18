import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.plot([1,2,3,4],[1,4,9,16],'g-o')
plt.title("Squares")
plt.subplot(1,2,2)
plt.plot([1,2,3,4],[1,8,27,64],'r-o')
plt.title("Cubes")
plt.suptitle("All plots")
plt.show()