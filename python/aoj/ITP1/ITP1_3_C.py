# encoding:utf-8
while True:
	input = map(int, raw_input().split())
	x, y = input
	if x == y == 0:
		break
	input.sort()
	print(" ".join(map(str, input))) 