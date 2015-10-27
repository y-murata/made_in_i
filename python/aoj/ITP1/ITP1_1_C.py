# encoding:utf-8

input = map(int, raw_input().split())

height, width = input
area = height * width
circumference = (height + width) * 2

print(" ".join(map(str, (area, circumference))))