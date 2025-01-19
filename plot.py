from matplotlib import pyplot as plt

x_values = [1,2,4,8,16,32]
y_values = [72.27,36.94,18.62,9.48,4.84,2.93]
plt.plot(x_values,y_values, marker='o')
plt.xticks([1,2,4,8,16,32])
plt.xlabel("numero thread")
plt.ylabel("tempo")
plt.grid(True) 
plt.yticks([72.27,36.94,18.62,9.48,2.93])
plt.show()