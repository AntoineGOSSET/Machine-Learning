import math

i = 2

while math.log(i) <= 1:
    print (math.log(i))
    print(i)
    i += 0.0001
print("A = %s" % (i))
    