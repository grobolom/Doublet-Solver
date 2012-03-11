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
	if x > y:
		return x
	return y

def search(word, target, all, depth):
	if depth > 10:
		return None
	children = oneaway(word, all)
	if target in children:
		return depth
	else:
		return False

