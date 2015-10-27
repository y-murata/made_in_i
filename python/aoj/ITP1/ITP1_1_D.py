# encoding:utf-8

input = input()

second = input % 60
minute = input / 60 % 60
hour = input / 60 / 60 % 60

print(":".join(map(str, (hour, minute, second))))