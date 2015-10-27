# encoding:utf-8

input = map(int, raw_input().split())
a, b, c = input

count = 0
for i in range(a, b+1):
	if c % i == 0:
		count += 1
print(count)