#lists

count = [1, 2, 3, 4, 5]
friuts = ['apple', 'oranges', 'peras', 'banana']
change = [1, 'mango', 2, 'pi-apple', 3, 'grapes']

for number in count:
	print "this is count %r" % number
for friut in friuts:
	print " friuts: %r" %friut

print cmp(count, change)
print len(friuts)	


full_name = []
for i in range (6,10):
	print "%r" %i
	full_name.append(i)
for i in full_name:
	print "%r" %i