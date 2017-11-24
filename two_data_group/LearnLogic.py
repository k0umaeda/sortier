import numpy as np
import ManageData as mng

class LearnLogic(mng.ManageData):
	def __init__(self, dim, elem_cnt, avg, data_group, bias):
		super().__init__(dim, elem_cnt, avg, data_group, bias)
		self.__classified = True
		self.__delta_weight = np.zeros(self.dim)
		self.__delta_bias = 0
	@property
	def classified(self):
		return self.__classified
	@classified.setter
	def classified(self, value):
		self.__classified = value
	@property
	def delta_weight(self):
		return self.__delta_weight
	@delta_weight.setter
	def delta_weight(self, value):
		self.__delta_weight = value
	@property
	def delta_bias(self):
		return self.__delta_bias
	@delta_bias.setter
	def delta_bias(self, value):
		self.__delta_bias = value	
	def learn(self):
		j = 1
		while True:
			self.classified = True
			for i in range(self.elem_cnt * self.data_group):
				self.delta_weight = (self.test_data(i) - self.y(self.x[i])) * self.x[i]
				self.delta_bias = (self.test_data(i) - self.y(self.x[i]))
				self.weight += self.delta_weight
				self.bias += self.delta_bias
				self.classified *= all(self.delta_weight == 0) * (self.delta_bias == 0)
				#self.classified *= (self.delta_weight[0] == 0) * (self.delta_weight[1] == 0) * (self.delta_bias == 0)
				#print(i)
				#print(self.classified)
				#if (i % (self.elem_cnt * self.data_group - 1) == 0) * (i != 0):
					#print("学習{0}:".format(j))
					#j += 1
					#print('delta_weight : ', end = '')
					#print(self.delta_weight)
					#print('weight : ', end = '')
					#print(self.weight)
					#print('delta_bias : ', end = '')
					#print(self.delta_bias)
					#print('bias : ', end = '')
					#print(self.bias)
					#print('classified : ', end = '')
					#print(self.classified)
					#print()
				if j > 10:
					print('Because of the proloned learning, the program was terminated.')
					break
			if self.classified:
				print("!!!! It is finishing to learn !!!!")
				print('weight : ', end = '')
				print(self.weight)
				print('bias : ', end = '')
				print(self.bias)
				break
