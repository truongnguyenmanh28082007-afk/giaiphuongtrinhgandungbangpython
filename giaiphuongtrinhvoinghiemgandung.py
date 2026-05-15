import numpy 
from scipy.optimize import fsolve


def hephuongtrinh(variables):
    x, y = variables
    f1 = x**2 + y*3 - 5
    f2 = x**3 - y**4 - 100
    return [f1, f2]

#
dudoan= [99,99] 

# Giải hệ phương trình
root = fsolve(hephuongtrinh, dudoan)

xbest, ybest = root

print(f"Nghiệm x xấp xỉ: {xbest:.4f}")
print(f"Nghiệm y xấp xỉ: {ybest:.4f}")

# Kiểm tra lại sai số
print(f"Sai số phương trình 1: {xbest**2 + ybest**3 - 5:.6f}")
print(f"Sai số phương trình 2: {xbest**3 - ybest**4 - 100:.6f}")
                                                 
