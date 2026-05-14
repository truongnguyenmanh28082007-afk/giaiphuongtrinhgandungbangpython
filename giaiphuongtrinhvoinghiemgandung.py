# x = (y**4 + 100)/ x**2 >= 0
# tách pt 1 thành { x, y}
                 #{ x, (5 - x**2)/3)}
# tách pt 2 thành { x, y}
                 #{ x, -(100 - x**3)**(1/4)}
# dùng công thức khoảng cách giữa 2 điểm ((x1 - x2)**2 + (y1 - y2)**2))**1/2
x = 0
def f(x):
     return abs(((5 - x**2)/3) + (100 - x**3)**(1/4))

for i in range(100000):
    x += 0.01  # (vì x dương)
    if f(x) < f(x + 0.01):
        break;
    
print("x =", x)


# y cũng làm tương tự như x
# y = -(100 - x**3)**(1/4) <= 0
# tách pt 1 thành { x, y}
                 #{ (5 - y*3)**(1/2), y}
# tách pt 2 thành { x, y}
                 #{ (100 + y**4)**(1/3), y}
# dùng công thức khoảng cách giữa 2 điểm ((x1 - x2)**2 + (y1 - y2)**2))**1/2
y = 0
def g(y):
     return abs(((5 - y*3)**(1/2)) - ((100 + y**4)**(1/3)))

for i in range(100000):
    y -= 0.01  # (vì y âm)
    if g(y) < g(y - 0.01):
        break;

print("y =",y)
                                             
