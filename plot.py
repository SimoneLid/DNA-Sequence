from matplotlib import pyplot as plt

x_values = [1,256,512,1024,2048,4608]
y_values = [1,1.76,4.98,5.98,10.83,8.73 ]
plt.plot(x_values,y_values, marker='o')
plt.xticks(x_values)
plt.yticks(y_values)
plt.grid(True)
plt.xlabel("numero thread")
plt.ylabel("speed up")
plt.show()