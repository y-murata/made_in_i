# encoding:utf-8
count = 1
while True:
	input = raw_input()
	if input == "0":
		break
	text = "Case " + ": ".join(map(str, (count, input)))
	print(text)
	count += 1