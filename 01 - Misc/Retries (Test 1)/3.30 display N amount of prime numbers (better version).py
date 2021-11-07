def disp_prime():
# enter the amount of prime numbers you want the program to display
    amount = int(input("How many prime numbers to display: "))
# first prime number is 2. Can't set it lower, because otherwise it will print
# numbers that aren't prime (1, 0, -1 , -2, etc.)
    prime = 2
# COUNTER for the amount of prime numbers
    i = 0
# WHILE-LOOP for the amount of prime numbers
    while i < amount:
# the FOR-LOOP essentially checks if the "prime" VARIABLE is divisible by numbers smaller than
# itself without a remainder
        for j in range(2, prime):
# check if the "prime" VARIABLE is divisible by a number from FOR-LOOP range without remainder
            if prime%j == 0:
# if there is no remainder FOR-LOOP breaks, stops working and skips to the next part
                break
# if the IF-STATEMENT was skipped or broken program executes the ELSE-STATEMENT
        else:
# print the "prime" variable and replace newline with a single space
            print(prime, end=" ")
# since the "prime" variable is a prime number, the counter is increased by 1 and
# the program looks for another prime number
            i += 1
# "prime" variable is increased by one to check whether another number is a prime number
        prime += 1


disp_prime()
