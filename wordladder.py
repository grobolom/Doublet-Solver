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

print oneaway(startword, words)
