# encoding:utf-8

while True:
	a, op, b = raw_input().split()
	if op == "?":
		break
	a, b = map(int, (a,b))
	if op == "+":
		print(a+b)
	elif op == "-":
		print(a-b)
	elif op == "*":
		print(a*b)
	else:
		print(a/b)