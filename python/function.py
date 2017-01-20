def print_two( *args):  #we end this line with a : colon, and start indenting.
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1, arg2)
	
def chandra(x,y):
	print "x: %r, y: %r" %(x,y)
	
def cheess_and_crakers(chees, crakers):
	print "chees : %r and crakers: %r" %(chees, crakers)
	
print_two("string1", "string2")
chandra("variable1", "variable2")
cheess_and_crakers(30,50) 