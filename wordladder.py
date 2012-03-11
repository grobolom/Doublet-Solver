def allwordsoflength(l):
	filename = '/usr/share/dict/words'
	words = [x.upper().strip() for x in open(filename) if len(x.upper().strip()) == l] 
	return words


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

# let's make something like this
# we have two lists
# first is the list containing all words we have created so far
# [ 'WOOD' ] to start

# the second is a list of tuples
# of the following format
# (word, depth, parents)

# so....

# we iterate by taking every word from every tuple in our second list
# and constructing the list of words that is one letter appart from said word
# then we remove from it every word that is in our 'done' list
# then we check if our target word is part of this set of words
# if it's not, we take our list of new words and append it to our second list
# using the depth +1 of our current word
# and the parents it lists. YAY BREADTH FIRST

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
	
