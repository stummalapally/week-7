import matplotlib.pyplot as plt

fig,ax=plt.subplots(ncols=2,nrows=2,figsize=(6,6))
ax[0,0].plot([1,2,3,4],[1,4,98,16],'g-o')
ax[0,0].set_xlabel("Numbers")
ax[0,0].set_ylabel("Squares")
ax[0,0].set_ylim(0,100)
ax[0,0].set_yticks(range(0,105,5))
ax[0,1].plot([1,2,3,4],[1,4,9,16])
ax[0,1].set_xlabel("0,1")
ax[0,1].set_ylabel("0,1")
ax[1,1].plot([1,2,3,4],[1,4,9,16])
ax[1,1].set_ylim(0,100)
ax[1,1].set_xlabel("1,1")

ax[1,1].set_ylabel("1,1")
plt.subplots_adjust(hspace=0.5)
plt.subplots_adjust(wspace=0.5)
plt.show()