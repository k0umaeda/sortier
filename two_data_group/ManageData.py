import numpy as np

class ManageData:
	def __init__(self, dim = 0, elem_cnt = 0, avg = 0, data_group = 0, bias = 0):
		self.__dim = dim
		self.__elem_cnt = elem_cnt
		self.__avg = avg
		self.__data_group = data_group
		self.__x = np.zeros((self.__elem_cnt * self.__data_group, self.__dim))
		self.__weight = np.zeros(self.__dim)
		self.__bias = 0
	@property
	def dim(self):
		return self.__dim
	@dim.setter
	def dim(self, value):
		self.__dim = value
	@property
	def elem_cnt(self):
		return self.__elem_cnt
	@elem_cnt.setter
	def elem_cnt(self, value):
		self.__elem_cnt = value
	@property
	def avg(self):
		return self.__avg
	@avg.setter
	def avg(self, value):
		self.__avg = value
	@property
	def data_group(self):
		return self.__data_group
	@data_group.setter
	def data_group(self, value):
		self.__data_group = value
	@property
	def x(self):
		return self.__x
	@x.setter
	def x(self, value):
		self.__x = value
	@property
	def weight(self):
		return self.__weight
	@weight.setter
	def weight(self, value):
		self.__weight = value
	@property
	def bias(self):
		return self.__bias
	@bias.setter
	def bias(self, value):
		self.__bias = value
	def step(self, __x):
 		return True * (__x > False)
	def test_data(self, __i):
		if __i < self.elem_cnt:
			return 0
		else:
			return 1
	def y(self, __x):
		return self.step(np.dot(self.__weight, __x) + self.__bias)
