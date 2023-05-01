# Test python env
def print_hello():
    animals = ['dog','cat','hamster'] #in one line
    food = [			
	'Spagetti',
	'Pizza'
	]	#in sevral lines without trailing comma

    names = [	 
	'Jhon',
	'Jane',
	'Gil-dong',
	]	#in sevral lines with triling comma
    for f_name in names : 
        print(f'hello, {f_name}')

if __name__ == '__main__' :
    print_hello()
