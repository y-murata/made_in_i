# encoding:utf-8

input = map(int, raw_input().split())
a, b = input

d = a / b
r = a % b
f = float(a) / b

print(d),
print(r),
print(('%03.8f' % f))