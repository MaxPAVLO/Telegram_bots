num = int(input())

def Fibonachi(num):
	if num == 1:
		return 0

	elif num == 2:
		return 1

	return Fibonachi(num - 1) + Fibonachi(num - 2)

for i in range(1, num + 1):
	print(Fibonachi(i))
