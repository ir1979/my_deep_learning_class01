# debug

# Error:   
#       1,2. Compile E.    -> (Lexical E.)   and     (Syntax E.)
#       3. Runtime E.      -> Exception      indefinite for loop
#       4. Logical E.      -> The result is not as expected!  ()


def SampleFunction(x, y):
    z = x/y
    return z

x = 12
y = 5

# z = x / y

z = SampleFunction(x, y)

print(z)



