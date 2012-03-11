startword = 'MOON'
endword = 'GOLF'

filename = '/usr/share/dict/words'
words = [x.upper().strip() for x in open(filename) if len(x.upper().strip()) == len(startword)]


