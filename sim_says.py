'''
	Problem: Simon Says
'''
N = int(input())
for i in range(N):
	string = input()
	if "Simon says" in string:
		print(string[len("Simon says") + 1:])