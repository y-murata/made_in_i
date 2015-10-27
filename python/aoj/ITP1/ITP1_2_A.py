# encoding:utf-8

input = map(int, raw_input().split())
a = input[0]
b = input[1]

if a == b:
	print("a == b")
elif a > b:
	print("a > b")
else:
	print("a < b")