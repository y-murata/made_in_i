# encoding:utf-8
import math

r = float(input())

area = r**2*math.pi
circumference = r * 2 * math.pi

area = ('%03.6f' % area)
circumference = ('%03.6f' % circumference)

print(area),
print(circumference)