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

def search(word, target, all, done, depth):
	if word == target:
		return [depth, target]
	if depth >= 10:
		return None
	children = oneaway(word, all)
	if set(children) < set(done):
		return None
	searchable = list(set(children) - set(done))
	words = []
	for nword in searchable:
		words.append(search(nword, target, all, list(set(searchable) | set(done)), depth + 1))
	if len(words) > 0:
		return reduce(red, words)
	return None

def newsearch(word, target, all, maxdepth):
	depth = 0
	done = []
	next = oneaway(word, all)
	while depth < maxdepth:
		if target in done:
			return depth
		done = next
		for x in next:
			done = list(set(done) | set(oneaway(x,all)))
		depth += 1
	return 'Not Found'

print newsearch('MOOD','WOOL',words,3)
