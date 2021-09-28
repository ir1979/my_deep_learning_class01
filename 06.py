import math

x = 10
y = 15

x,y = y,x

print(f'x={x}, y={y}')

list1 = ['ali', 'hasan']
list2 = list1[:]    # copy

# tuple
center_point = (0,0)
print(center_point[0])
# center_point[0] += 1  # error
center_point = (5,10)

##########################3
#  <   >   ==   !=   <=   >=
# and or not   
# & | !

if (x+y<10) & (x+y < 100):
    print(x+y)

#if x>=5 and x<=10:
if 5 <= x <= 10:
    pass
elif 2 <= y <= 100:
    print('very good')
else:
    print('not ok')


a = int(input('A'))
b = int(input('B'))
c = int(input('C'))


delta = b**2-4*a*c

if delta>0:
    x1, x2 = -b+math.sqrt(delta)/2/a, -b-math.sqrt(delta)/2/a
elif delta==0:
    x1 = x2 = -b/2/a
else:
    x1 = x2 = None


print(f'x1: {x1}, x2: {x2}')


