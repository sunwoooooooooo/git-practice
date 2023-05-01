# Test python env
def print_hello():
    animals = ['dog','cat','hamster','tiger'] #in one line
    food = [			
	'Spagetti',
	'Pizza',
	'Bibimbab'
	]	#in sevral lines without trailing comma

    names = [	 
	'Jhon',
	'Jane',
	'Gil-dong',
	'Dong-eun',
	]	#in sevral lines with triling comma
    for f_name in names : 
        print(f'hello, {f_name}')

if __name__ == '__main__' :
    print_hello()
