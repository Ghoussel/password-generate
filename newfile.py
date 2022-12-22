import random,string
with open('pass.txt', 'w') as f:
	for i in range(1000):
		f.write(''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8,13))))
		f.write('\n')
		print ('done')