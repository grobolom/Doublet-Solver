startword = 'MOON'
endword = 'GOLF'

filename = '/usr/share/dict/words'
words = [x.upper().strip() for x in open(filename) if len(x.upper().strip()) == len(startword)]

def oneletteroff(a,b):
	one = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			one += 1
		if one > 1:
			return None
	return 1

def oneaway(word, all):
	return [x for x in all if oneletteroff(word, x)]

def red(x,y):
	if x == None:
		return y
	if isinstance(x,list) and isinstance(y,list):
		if x[0] < y[0]:
			return x
		return y
	return x

def search(word, target, all, depth):
	if word == target:
		return [depth, target]
	if depth >= 4:
		return None
	children = oneaway(word, all)
	words = []
	for nword in children:
		words.append(search(nword, target, all, depth + 1))
	return reduce(red, words)

print search('MOON', 'WOLF', words, 0)
