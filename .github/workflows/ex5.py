my_name ='Randall'
my_age=40 # not a lie
my_height= 69 * 2.54 # inches
my_weight= 185.0 / 2.2 # lbs
my_eyes= 'browm'
my_teeth='White'
my_hair='black'

print "%r let's talk about %s." % my_name
print "he's %d cm tall." % my_height
print "he's %d pound heavy" % my_weight
print "actually that's not too heavy"
print "he's got %s etes %s hair" % (my_eyes, my_hair)
print "his teeth are ussually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "if i add %d %d %d, and %d i get %d" % (
my_age, my_height, my_weight, my_age + my_height + my_height)