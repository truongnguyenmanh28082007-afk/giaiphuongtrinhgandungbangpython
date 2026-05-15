import numpy 
from scipy.optimize import fsolve

# hệ phương trình
def hephuongtrinh(variables):
    x, y = variables
    f1 = x**2 + y*3 - 5
    f2 = x**3 - y**4 - 100
    return [f1, f2]

# khởi tạo giá trị dự đoán ban đầu cho x và y
# nên chọn giá trị dự đoán sao cho gần với nghiệm của pt mũ lớn hơn
# x^3 - y^4 - 100 = 0 => x = 5, y = -2 hoặc y = 2 
# x^2 + y*3 - 5 = 0 => x = 5, y = -2
dudoan= [5,-2] 

# giải hệ phương trình
root = fsolve(hephuongtrinh, dudoan)

xbest, ybest = root

print(f"x: {xbest:.4f}")
print(f"y: {ybest:.4f}")

# Kiểm tra lại sai số
print(f"sai số f1:{xbest**2 + ybest*3 - 5:.6f}")
print(f"sai số f2: {xbest**3 - ybest**4 - 100:.6f}")
                                           
