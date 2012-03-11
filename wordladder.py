def allwordsoflength(l):
	filename = '/usr/share/dict/words'
	words = [x.upper().strip() for x in open(filename) if len(x.upper().strip()) == l] 
	return words

def oneletteroff(a,b):
	one = 0
	for i,j in map(None, a, b):
		if i != j:
			one += 1
		if one > 1:
			return None
	return 1

def oneaway(word, all):
	return [x for x in all if oneletteroff(word, x)]

def search(start, end, maxdepth = 20):
	ftree = [(start, 0, [])]
	done = [start]
	all = allwordsoflength(len(start))

	for e in ftree:
		if e[1] > maxdepth:
			return 'Reached Max Depth.' 

		children = oneaway(e[0], all)
		children = list(set(children) - set(done))
		if children == [] and e == ftree[-1]:
			return 'Search Exhausted.' 

		if end in children:
			return (e[1] + 1, ' '.join(e[2] + [e[0], end]))

		for n in children:
			ftree.append((n, e[1] + 1, e[2] + [e[0]]))
		
		done = list(set(done) | set(children))

print search('PIG','STY')
print search('OAT','RYE')
print search('CHIN','NOSE')
print search('PITY','GOOD')
print search('PITCH','TENTS')
print search('FLOUR','BREAD')
print search('COLD','WARM')
	
