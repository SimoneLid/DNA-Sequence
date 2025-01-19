from matplotlib import pyplot as plt

x_values = [32,64,96,128,160,192,224,256]
y_values = [2.297742,1.193476,0.826267,0.788565,0.636911,0.526974,0.503687,0.449722]
plt.plot(x_values,y_values, marker='o')
plt.xticks([32,64,96,128,160,192,224,256])
plt.xlabel("numero thread")
plt.ylabel("tempo (caso migliore)")
plt.grid(True) 
plt.yticks([2.297742,1.193476,0.826267,0.636911,0.526974,0.449722])
plt.show()