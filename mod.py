'''
	Problem: Modulo
'''
mods = []
for i in range(10):
	num = int(input())
	if num % 42 not in mods:
		mods.append(num % 42)

print(len(mods))