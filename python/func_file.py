from sys import argv

script, file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0,15)

def print_a_line(line_count,f):
	print line_count, f.readline()
	
current_file = open(file)

print_all(current_file)

rewind(current_file)

current_line = 1
print_a_line(current_line,current_file)
current_line = 2
print_a_line(current_line,current_file)