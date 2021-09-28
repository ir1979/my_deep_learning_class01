import math
from tqdm import tqdm


x = 5

if x==5:
    x+=1


print('Salam')
print('x = ', x)

print(f'x = {x}')
print(f'x = {math.sin(x)}')

x = 'ali' 
          
x = "hasan   \
             \
            \"Fatemeh\" "

print(x)

x = """zahra is
    here"""

print(f"""x = {x}""")



y = 'x' * 80
print(y)

z = 5/2    #  2.5
z = 5//2   #  2
z = -5//2  #  -3
z = 5%2    # 1
z = -5%2   # 1
z = 5%-2   # -1


################ lists ##############
list1 = [1,2,3,4]
list1[0] = 5
list1[1] = 'ali'
list1 +=  ['hasan']
list1.remove(4)
list1.pop(2)
list1.insert(1,"sajad")
del list1[0]

list2 = []
for i in range(1,10,1):
    list2+= [i*i]

# list comprehension
list3 = [2**i for i in range(1,10,1) if i%2==1]


list4 = [[1,2], ["ali", "hasan", "hossein"], []]
print(list4[0][1])


list5 = [[1,2,3], [4,5,6], [7,8,9]]
list6 = [[i for i in range(j,j+3,1)] for j in range(1,10,3)]

print(list6)

for element in list5:
    print(element[0], end=' ')
print()


list7 = [x for row in list5 for x in row]
print(list7)



list8 = [j for j in range(20)]
print(list8)
print(list8[0:5])
print(list8[-1])
print(list8[-2:])
print(list8[2:9:2])
print(list8[::-1])    # 


list9 = list8[:]  # copy
list8[0] = 11
print(list9)


tpl1 = (1,2,3)
print(tpl1[1])
# tpl1[1] = 5       # error

print(tpl1)

tpl2 = ((1,2), (2,3))
print(tpl2[0:1])     #   2

tpl2 = tpl1




for i in tqdm(range(100)):
    for j in range(1000000):
        pass    





print("Finished!")

#    
