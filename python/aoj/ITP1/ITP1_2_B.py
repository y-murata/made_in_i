# encoding:utf-8

input = map(int, raw_input().split())
a, b, c = input

if a < b and b < c:
	print("Yes")
else:
	print("No")