from collections import defaultdict
import urllib2

def allwords():
	filename = '2of12inf.txt'
	filename2 = '/usr/share/dict/words'
	words = [x for x in open(filename)]	
	words += [x for x in open(filename2)]
	return words 

def allwordsoflength(l, all):
	return set([x.upper().strip() for x in all if len(x.upper().strip()) == l])

def wildcard(s, idx):
    return s[:idx] + '?' + s[idx+1:]

def wildcarded(s):
    for idx in xrange(len(s)):
        yield wildcard(s, idx)

def buildindex(all):
	index = defaultdict(list)
	for w in all:
		for wild in wildcarded(w):
			index[wild.upper()].append(w)
	return index

def oneaway(word, index):
	ret = []
	for w in wildcarded(word):
		ret += index[w]
	return ret

def search(start, end, all, maxdepth = 10):
	ftree = [(start, 0, [])]
	done = [start]
	alloflen = allwordsoflength(len(start), all)
	index = buildindex(alloflen)

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


all = allwords()
print search('PIG','STY', all)
print search('OAT','RYE', all)
print search('CHIN','NOSE', all)
print search('PITY','GOOD', all)
print search('PITCH','TENTS', all)
print search('FLOUR','BREAD', all)
print search('COLD','WARM', all)
	
