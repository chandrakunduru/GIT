# It presents a prompt to the user (the optional arg of raw_input([arg])), gets input from the user and returns the data input by the user in a string.
name = raw_input("What is your name? ")
print "Hello, %s." % name

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()