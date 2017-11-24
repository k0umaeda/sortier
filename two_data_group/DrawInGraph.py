import numpy as np
import matplotlib.pyplot as plt

# グラフを描画するクラス 
class DrawInGraph():
	# 2次元の散布図を描画
	def two_dim_scatter(__x, __y):
		plt.scatter(__x[0], __x[1], c = "red")
		plt.scatter(__y[0], __y[1], c = "blue")
	def two_dim_smooth_line(__x, __y):
		plt.plot(__x, __y)
