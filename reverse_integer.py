

# 6371 -> 1736
# 6371 divide by 10 => 6371 = 637*10 + 1
#                       637 = 63*10 + 7
#                        63 = 6*10 + 3
#                         6 = 0*10 + 6
# take 1736 as output

# Simple step
# num = int(input("Enter Number = "))
# division1 = num//10
# #print(division1)
# r1 = num%10
# division2 = division1//10
# #print(division2)
# r2 = division1%10
# division3 = division2//10
# #print(division3)
# r3 = division2%10
# division4 = division3//10
# #print(division4)
# r4 = division3%10
# print(r1,r2,r3,r4)

# Second Way 
num = int(input("Enter number = "))
reverse = 0 # i dun have reverse variable 
while num != 0 :  # my previous code while True: infinite loop
    remainder  = num%10
    reverse = reverse*10 + remainder
    num = num//10
    
print(reverse)




