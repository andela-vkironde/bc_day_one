def gen_prime_numbers(n):

    """ Function to generate prime numbers within a certain range
    and append them to a list """
    list_of_prime_numbers = []

    if n is not None:
        if n > 0:
            for value in range(0, n):
                if value % 2 == 0:
                    list_of_prime_numbers.append(value)
                else:
                    pass
            return (list_of_prime_numbers)
        else:
            return("Error: Input positive number")
    else:
        return("Error: Invalid input")
