x = "There are %d types of people." % 10 # comentario declaro variable 
binary = "binary" # declaro variable
do_not = "don't"
y = "those who know %s and those who %s ." % (binary, do_not)

print x # imprimo variable
print y

print "I said: %r " % x
print "I also said: '%s'. " % y

hilarios = False
joke_evaluation ="isn't that joke so funny ! %r"

print joke_evaluation % hilarios

w = "this is the left side of..."
e = "a string with a right side"

print w + e