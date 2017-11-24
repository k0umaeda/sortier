import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(123)

d = 2
N = 10
avg = 5

x1 = rng.randn(N, d) + np.array([0, 0])
x2 = rng.randn(N, d) + np.array([avg, avg])
x = np.concatenate((x1, x2), axis = 0)

#x1_draw = np.transpose(x1)
#x2_draw = np.transpose(x2)

x1 = np.transpose(x1)
x2 = np.transpose(x2)

#plt.scatter(x1[0], x1[1], c = 'red')
#plt.scatter(x2[0], x2[1], c = 'blue')
#plt.show()

w = np.zeros(d)
b = 0
j = 0

def y(x):
	return step(np.dot(w, x) + b)
def step(x):
	return 1 * (x > 0)
def t(i):
	if i < N:
		return 0
	else:
		return 1
while True:
	classified = True
	for i in range(N * 2):
		delta_w = (t(i) - y(x[i])) * x[i]
		delta_b = (t(i) - y(x[i]))
		w += delta_w
		b += delta_b
		classified *= all(delta_w == 0) * (delta_b == 0)
#		if (i % (N * 2)) == 0:
#			j += 1
#			print('step : j', format(j))
#			print(delta_w)
#			print(delta_b)
#			print(classified)
#			print()
	if classified:
		print(w[0])
		print(w[1]) 
		x2 = (-1) *  w[0] * x1 - b / w[1]
		plt.scatter(x1[0], x1[1], c = 'red')
		plt.scatter(x2[0], x2[1], c = 'blue')
		plt.plot(x1, x2)
		plt.show()
#			print(y([0, 0]))
#			print(y([5, 5]))
#			print()	
		break
