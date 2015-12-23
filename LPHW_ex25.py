#This is exercise 25 of learn python the hard way
# It is practice of funcitons in python
# THese functions are to be run from an interactive python terminal
#This function uses the dot operator and the split function to split strings based on defined character
def break_words(stuff):
	"""THIS FUCNTION WILL BREAK UP WORDS FOR US."""
	words = stuff.split(' ')
	return words

#uses sort function to sort the array of "words"
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

#uses pop function with the dot operator to remove the first word from the list
def print_first_word(words):
	"""PRINTS the first word after popping it off."""
	word = words.pop(0) #removes word from zero position of list
	print word

# prints the last word of the list after removing it
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1) #removes word from -1 (last) position of list
	print word

#Sorts words of sentence and returns a sorted list
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence) #uses the break_words function to break up the sentence into a list
	return sort_words(words) #uses previously defined sort_words function to sort the words list

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words) #uses the print_first_word function previously defined to print the first word and remove it from the list
	print_last_word(words) #uses print_last_word function to print last word of list and remove it

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words) #prints first word from sorted list
	print_last_word(words) #prints last word from sorted list
