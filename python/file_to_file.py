from sys import argv
from os.path import exists

script, first_file , second_file = argv

print " copy from %r to %r" % (first_file,second_file)

data = open(first_file)
firstdata = data.read()

print " first_file of length %r", len(firstdata)

print "Does the output file exist? %r" % exists(second_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

second_data = open(second_file, 'w')
second_data.write(firstdata)

change = open(second_file)
print change.read()