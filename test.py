	#Define a function called generate_evens
def generate_evens():
	x = 2
	even_list = []
	while x < 50:
		even_list.append(x)
		x += 2
	return even_list	
#It should return a list of even numbers between 1 and 50(not including 50)

print(generate_evens())

