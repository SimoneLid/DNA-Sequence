from matplotlib import pyplot as plt

x_values = [1,64,128]
y_values = [14.357179,0.572506,0.2725]
plt.plot(x_values,y_values, marker='o')
x1_values = [1,4,16,32]
y1_values = [14.357179,3.944204,1.268656,0.853488]
plt.plot(x1_values,y1_values, marker='o')
plt.xlabel("numero thread")
plt.ylabel("tempo")
plt.show()