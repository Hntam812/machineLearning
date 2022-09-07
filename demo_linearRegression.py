from genericpath import samefile
from random import sample
import numpy as np
import matplotlib.pyplot as plt

#Phát sinh dữ liệu

x=np.arange(-5,5,0.5)

#tổng số mẫu
n_sample= len(x)

#Tạo nhiễu cho hàm y: 
#noise = np.random.normal(mu , sigma, n)
#mu : trung bình sẽ là 0, noise sẽ dao động quanh vị trí cb 0
#sigma: mức độ nhiễu, biên độ
#n số mẫu

noise = np.random.normal(0, 1, n_sample)

#y=w1*x  + w0  +  noise
y=5*x-6+noise

#vẽ y : 
#plt.plot(x,y) #tạo ra đường thẳng 
plt.plot(x,y, 'ro')


# # Khởi tạo tham số 
# w0=10
# w1=-4
# alpha=0.01
# eps=0.001


# #Lặp 
# while True: 
#     dw0=np.mean(x*w1+w0-y)
#     dw1=np.mean((x*w1+w0-y)*x)
    
#     w0=w0-alpha*dw0
#     w1=w1-alpha*dw1
    
#     #Trực quan hóa : vẽ phương trình đường thẳng y
#     x_visual=np.array([-5,5])
#     y_visual=w1*x_visual+w0
#     plt.plot(x_visual,y_visual)
#     plt.pause(0.1)
    
#     #Cập nhật tham số
#     dw0=np.mean(x*w1+w0-y)
#     dw1=np.mean((x*w1+w0-y)*x)
    
#     #Kiểm tra điểm dừng của vòng lặp
#     if(abs(dw0)< eps and abs(dw1)<eps):
#         break


# #Hiển thị kêt quả
# print("Gía trị tối ưu của w0 : " , w0)
# print("Gía trị tối ưu của w1 : " , w1)
plt.show()