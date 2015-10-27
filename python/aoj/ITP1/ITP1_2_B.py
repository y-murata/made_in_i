# encoding:utf-8

input = map(int, raw_input().split())
a = input[0]
b = input[1]
c = input[2]

if a < b and b < c:
	print("Yes")
else:
	print("No")