
# what is prime number?
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Prime number are 2, 3, 5, 7 Ex: 2 = 2x1, 3 = 3x1, 5 = 5x1, 7 = 7x1

# like 4 = 2x2 = 4x1 
# like 6 = 2x3 = 6x1
# like 8 = 2X2x2 = 2x4 = 8x1
# Note: every prime number are division of non prime number 
#############################

Lower_interval = int(input('Enter Lower Number = '))
Last_interval = int(input('Enter Last Number =  '))
print("\n########################################")
print("\n Prime Number are: \n")

for prime_number in range (Lower_interval, Last_interval+1):
    if prime_number > 1:
        for prime_division in range (2, prime_number):
            if (prime_number % prime_division) == 0:
                break
        if (prime_number % prime_division) == 1:
            print(prime_number)


############################
