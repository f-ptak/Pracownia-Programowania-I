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
# the FOR-LOOP is used for checking if the "prime" VARIABLE is divisible without a remainder.
#
### if the "prime" VARIABLE is 2 or 3, the FOR-LOOP range is (2,2). It can't be executed, so
### the program skips the FOR-LOOP and executes the ELSE-STATEMENT
#
# if the "prime" VARIABLE is 4, the FOR-LOOP range is (2,3). It can be executed, so
# the program executes the IF-STATEMENT. The IF-STATEMENT checks if the VARIABLE is
# divisible by 2 without a remainder. Since there is no remainder the program executes the IF-STATEMENT and
# BREAKS skipping the ELSE-STATEMENT
#
### if the "prime" VARIABLE is 5, FOR-LOOP range is (2,3). It can be executed, so the program
### checks if the VARIABLE is divisible by 2 without remainder. Since there is a remainder
### the program doesn't execute the IF-STATEMENT and skips to the ELSE-STATEMENT
# 
# etc. etc.
# the FOR-LOOP essentially checks if the "prime" VARIABLE is divisible by numbers smaller than
# itself without a remainder
        for j in range(2, (prime//2)+1):
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