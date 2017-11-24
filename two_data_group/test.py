import numpy as np
import matplotlib.pyplot as plt
import LearnLogic as lrn
import DrawInGraph as dg

rng = np.random.RandomState(123)
model_data = lrn.LearnLogic(dim = 2, elem_cnt = 1000, avg = 5, data_group = 2, bias = 0)
input_rng = rng.randn(model_data.elem_cnt, model_data.dim)

#print(model_data.dim)

# 入力データの設定
x1 = input_rng
x2 = input_rng + np.array([model_data.avg, model_data.avg])
model_data.x = np.concatenate((x1, x2), axis = 0)
#print(model_data.x)

# 学習開始
print('Learning...')
model_data.learn()

# 学習終了後グラフを表示
	# 2点で近似するため，xの任意の2点を定義
x_area = [-model_data.avg, model_data.avg + (model_data.avg / 2)]
	# 出力yの式を任意の2点の関数として定義
x1_res = -1 * ((model_data.weight[0] * x_area[0] + model_data.bias) / model_data.weight[1])
x2_res = -1 * ((model_data.weight[0] * x_area[1] + model_data.bias) / model_data.weight[1])
class_line = [x1_res, x2_res]
# 描画
dg.DrawInGraph.two_dim_scatter(x1.T, x2.T)
dg.DrawInGraph.two_dim_smooth_line(x_area, class_line)
plt.show()
