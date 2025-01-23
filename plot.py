from matplotlib import pyplot as plt

x_values = [(i+1)*32 for i in range(8)]
y_values = [20.701264,39.412316,56.375261,65.457084,83.444366,94.372852,102.075892,110.166819]
y_values2 = [28.093663,53.65832,71.251332,84.816259,95.208324,106.580888,94.790197,110.166819]
plt.plot(x_values,y_values2, marker='o')
plt.plot(x_values,y_values, marker='o')
plt.xticks(x_values)
plt.yticks(y_values)
plt.grid(True)
plt.xlabel("thread (in totale)")
plt.ylabel("tempi")
plt.show()