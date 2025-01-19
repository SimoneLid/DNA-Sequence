from matplotlib import pyplot as plt

x_values = [1,2,4,8,16,32]
y_values = [71.273433,36.941176,18.620522,9.486428,4.841522,2.939143]
plt.xticks([1,2,4,8,16,32])
plt.yticks([71.273433,36.941176,18.620522,9.486428,4.841522,2.939143])
plt.grid()
plt.plot(x_values,y_values, marker='o')
plt.xlabel("numero thread")
plt.ylabel("tempo")
plt.show()