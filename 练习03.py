num = int(input('>>>'))

def func():
	res = [1]
	while True:
		yield res
		res = [1] + [res[i] + res[i+1] for i in range(len(res)-1)] + [1]

y = func()
print('[')
for var in range(num):
	print(next(y))
print(']')
