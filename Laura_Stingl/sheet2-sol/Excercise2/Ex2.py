# Sheet 2 Excercise 2(3.5points/4points) 
#comment-The plot of R2ee and N will be a straight line, when you use the same code for different values of N analyse, please remember to refresh your code , this effect(in the plot(Plot will be little look like a straight line(not exactly)) is coming out due to that 
# Laura Stingl

import numpy
import math
import matplotlib.pyplot as plt

# adjust if necessary
# files are included in solution
path = ''

N = [200, 400, 600, 800, 1000]

# (b) calculate R2ee
avg = numpy.zeros(len(N))
for i in range(len(N)):
    f_np = numpy.loadtxt(path + 'analyse-n' + str(N[i]))
    sum = numpy.sum(f_np, axis=0)[1]
    length = f_np.shape[0]
    avg[i] = sum/length

print(avg)
#solution: [2780.58572082 2204.41933913 2212.99604964 2450.0640038  2862.93626056]


#"""
# (c) plot R2ee(N), plot is included in solution
plt.plot(N, avg)
plt.xlabel('N')
plt.ylabel('R2ee(N)')
plt.title('Sheet 2 Exercise 2c')
plt.savefig('Sh2_Ex2_c')
plt.show()
#"""

# (c) determine ny
ny = numpy.zeros(len(N))
for i in range(len(N)):
    ny[i] = math.log(avg[i], N[i])/2

print(ny)
#solution: [0.74839013 0.64243219 0.60201557 0.58371898 0.57613528]
