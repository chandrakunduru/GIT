from sys import argv

prog, name = argv
chandra = '>>'

print "hi %r i'm the %r prog." %(name, prog)
print "I'd like to ask you a few questions."
print "Do you like mr %r?" % name
likes = raw_input(chandra)

print "where do you live %s?" % name
lives = raw_input(chandra)

print "what knid of computer do have?"
computer = raw_input(chandra)

print """ %r %r %r""" % (likes, lives, computer)