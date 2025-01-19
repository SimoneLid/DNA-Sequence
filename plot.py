from matplotlib import pyplot as plt

x_values = [1,2,4,8,16,32]
y_values = [1,1.928686,3.826311,7.51051,14.716016,24.241052]
plt.plot(x_values,y_values, marker='o')
plt.xticks([32,64,96,128,160,192,224,256])
plt.xlabel("numero thread")
plt.ylabel("speedup")
plt.show()