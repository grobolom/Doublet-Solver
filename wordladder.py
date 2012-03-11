from collections import defaultdict

def allwordsoflength(l):
	filename = '/usr/share/dict/words'
	words = set([x.upper().strip() for x in open(filename) if len(x.upper().strip()) == l])
	return words

def wildcard(s, idx):
    return s[:idx] + '?' + s[idx+1:]

def wildcarded(s):
    for idx in xrange(len(s)):
        yield wildcard(s, idx)

def buildindex(all):
	index = defaultdict(list)
	for w in all:
		for wild in wildcarded(w):
			index[wild].append(w)
	return index

def oneaway(word, index):
	ret = []
	for w in wildcarded(word):
		ret += index[w]
	return ret

def search(start, end, maxdepth = 20):
	ftree = [(start, 0, [])]
	done = [start]
	all = allwordsoflength(len(start))
	index = buildindex(all)

	for e in ftree:
		if e[1] > maxdepth:
			return 'Reached Max Depth.' 

		children = oneaway(e[0], index)
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
	
