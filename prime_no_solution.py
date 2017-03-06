def gen_prime_number(n):
	if n is not None:
	    if n > 0:
	    	for value in range (0,n):
	    		if value % 2 == 0:
	    			print (value)
	    		else:
	    			pass
	    else:
	    	return("Error: Input positive number")
	else:
		return("Error: Invalid input")
