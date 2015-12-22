#This file is a clone of excersise 24 from learn python the hard way by zed shaw
# This is a python script with the extention .py
# it is a review of many of the basic functions in the course

print "Let's practice everything."
#Escapes
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

#creating "poem" variable that will be used to print later, shows user how to save text in a variable
#Triple quotes in python mean that you can type across lines and will be saved as string
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovelynor comprehend passion form intuition
and requires an explanaiton
\n\t\t where there is none.
"""
print "----------------------"
#print out the poem
print poem
print "----------------------"

# doing math on variables
five = 10 - 2 + 3 - 6
#Print this number as a string
print "this should be five: %s" % five

# Define the secret formula function
def secret_formula(started): #Function takes in started number
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates # returns values of each of the variables that used started variable

start_point = 10000
beans, jars, crates = secret_formula(start_point) #start point is used in place of started, saves values in beans, jars, crates

print "With a starting point of: %d" % start_point 
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates) # values created previously on line 36

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, %d crates." % secret_formula(start_point) # this runs the funciton differently not creating global instances of the variables used
