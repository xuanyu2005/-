import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体为黑体，使中文能正常显示（需系统有对应字体支持，若没有可替换为其他可用中文字体）
plt.rcParams['font.sans-serif'] = ['SimHei']  
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False  

# 条纹移动数
k = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
# 副光栅位置读数（单位：mm）
Lk = np.array([105.666, 103.467, 100.941, 98.455, 95.923, 93.467, 90.792, 88.399, 85.772, 83.295])
L0 = Lk[0]  # 初始位置读数

# 计算位移ΔLk
delta_Lk = np.abs(Lk - L0)

# 输出计算后的位移ΔLk
print("条纹移动数k对应的位移ΔLk（单位：mm）:")
for i in range(len(k)):
    print(f"k={k[i]}时，ΔLk={delta_Lk[i]}")

# 拟合直线，获取斜率等拟合参数
fit_params = np.polyfit(k, delta_Lk, 1)
slope = fit_params[0]  # 直线斜率

# 绘制散点图和拟合直线
plt.scatter(k, delta_Lk, label='数据点')
plt.plot(k, np.polyval(fit_params, k), 'r', label='拟合直线')
plt.xlabel('条纹移动数 k')
plt.ylabel('位移 ΔLk (mm)')
plt.title('用直线光栅测量线位移条纹移动数与位移的关系')

# 调整直线解析式的输出位置，这里选择放置在图像的中间，可根据实际需求灵活调整坐标值
# x坐标选择一个稍大于横坐标最大值的位置，y坐标选择稍大于纵坐标最大值的合适位置
x_text = max(k) * 1.1  
y_text = max(delta_Lk) * 1.05  
plt.text(x_text, y_text, f'y = {slope:.3f}x', fontsize=12) 

plt.legend()
plt.show()

# 已知的光栅常数值（单位：mm）
d_known = 0.500
# 计算相对误差
relative_error = np.abs((slope - d_known) / d_known) * 100
print(f"相对误差为：{relative_error}%")