# encoding:utf-8

input = map(int, raw_input().split())
W, H, x, y, r = input

if x - r < 0 or x + r > W:
	print("No")
elif y - r < 0 or y + r > H:
	print("No")
else:
	print("Yes")