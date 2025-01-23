from matplotlib import pyplot as plt


num_thread_omp = [1,2,4,8,16,32]
times_omp = [0.108047,0.04031,0.032786,0.020494,0.015392,0.015913]
speedup_omp =[1,2.680402,3.295522,5.272128,7.019686,6.789857]

num_thread_MPI = [1,32,64,96,128,160,192,224,256]
times_MPI = [0.108047,0.010282,0.011096,0.01115 ,0.009412,0.011159,0.010705,0.013036,0.012995]
speedup_MPI = [1,10.508364,9.7374,9.690314,11.479707,9.682498,10.093134,8.288355,8.314506]


x_values = num_thread_MPI
y_values = times_MPI

plt.grid(True)
plt.plot(x_values,y_values, marker='o')
plt.xticks(x_values)
plt.yticks([0.108047,0.009412])
plt.xlabel("numero thread")
plt.ylabel("tempo")

plt.show()