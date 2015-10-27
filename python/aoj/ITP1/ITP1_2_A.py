# encoding:utf-8

input = map(int, raw_input().split())
a, b = input

if a == b:
	print("a == b")
elif a > b:
	print("a > b")
else:
	print("a < b")