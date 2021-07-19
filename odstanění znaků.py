import os

	string = open('demofile.txt').read()
	new_str = re.sub(b,'', string)
	open("demofile.txt"'w').write(new_str)
