# file_reading and writing

from sys import argv

script, filename = argv

print "we are going to erase %r" % filename
#raw_inupt("?")

print "opening the file...."
chandra = open(filename, 'w')

#print "trucation the file. GOOD bye"
#chandra.truncate()

print "now i'm going to write the file"
line1 = raw_input("line1:")
chandra.write(line1)
chandra.write("\n")
line2 = raw_input("line2:")
chandra.write(line2)

chandra = open(filename)
print chandra.read()

chandra.close()






