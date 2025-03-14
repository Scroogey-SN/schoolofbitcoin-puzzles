#!/bin/env python3

import copy, itertools

# You have all the clues needed ... from how you got here... 
# Hidden on this card... is every clue needed to find a treasure of...

words = ['can', 'you', 'solve', 'the', 'puzzle', 'and', 'find', 'sats',
    'school', 'of', 'bitcoin', 'who', 'will', 'claim', 'hidden', 'treasure',
    'it', 'be', 'has', 'anyone', 'found', 'yet', 'scan', 'to', 'enter',
    'please', 'follow', 'us', 'on', 'this', 'card', 'is', 'every', 'clue',
    'needed', 'one', 'million', 'good', 'hunting', 'miss' ]

# every letter a will be capital A
def capitalizeA(wl):
	for i in range(0, len(wl)):
		wl[i] = wl[i].replace('a', 'A')

# put a + symbol between each word
def plusBetween(wl):
	for i in range(0, len(wl) - 1):
		wl[i] = wl[i] + '+'

# every g will now be double g.. ie. gg
def doubleG(wl):
	for i in range(0, len(wl)):
		wl[i] = wl[i].replace('g', 'gg')

# put a ! symbol before every word
def exclamBefore(wl):
	for i in range(0, len(wl)):
		wl[i] = '!' + wl[i]

# put each word in brackets
def inBrackets(wl):
	for i in range(0, len(wl)):
		wl[i] = '[' + wl[i] + ']'

# replace any b with the number 6
def bto6(wl):
	for i in range(0, len(wl)):
		wl[i] = wl[i].replace('b', '6')

# put ##1 at the end of the words indicating my most important password
def suffix(wl):
	wl[len(wl) - 1] += '##1'

# put a comma between each word
def commaBetween(wl):
	for i in range(0, len(wl) - 1):
		wl[i] = wl[i] + ','

# replace any letter s with a 5
def sto5(wl):
	for i in range(0, len(wl)):
		wl[i] = wl[i].replace('s', '5')

funcs = [ capitalizeA, plusBetween, doubleG, exclamBefore, inBrackets, bto6, suffix, commaBetween, sto5 ]

# choose 4 or 5 words
#for words_combination in list(itertools.chain.from_iterable(itertools.combinations(words, i) for i in range(4, 6))):
for words_combination in list(itertools.chain.from_iterable(itertools.combinations(words, i) for i in range(4, 5))):
	for words_permutation in list(itertools.permutations(words_combination)):
#		# pick 2 or 3... no more!
#		for funcs_combination in list(itertools.chain.from_iterable(itertools.combinations(funcs, i) for i in range(2, 4))):
#			for funcs_permutation in list(itertools.permutations(funcs_combination)):
				funcs_permutation = [ capitalizeA, plusBetween ]
				wl = copy.deepcopy(list(words_permutation))
				for func in funcs_permutation:
					func(wl)
				# if capitalizeA wasn't used, skip
				if ''.join(wl).count('A') > 0:
					print(''.join(wl))

# 4-5 words, 2-3 functions: (40*39*38*37+40*39*38*37*36)*(9*8+9*8*7) = 46744888320 (7411 years)
# 4 words, 2 functions: 40*39*38*37*9*8 = 157921920 (25 years)
# 4 words, 2 given functions: 40*39*38*37 = 2193360, 1535640 contain 'a' (89 days)

