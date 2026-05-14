# bên dương
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
      
    
print("x1 =", x)
y = (5 - x**2)/3
print("y1 =", y)

#bên âm
x = 0

for i in range(100000):
  x -= 0.01
  if f(x) < f(x - 0.01):
      break

print("x2 =",x)
y = (5 - x**2)/3
print("y2 =",y)
                                                 
