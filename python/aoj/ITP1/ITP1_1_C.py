# encoding:utf-8

input = map(int, raw_input().split())
height = input[0]
width = input[1]
area = height * width
circumference = (height + width) * 2
print(area),
print(circumference)