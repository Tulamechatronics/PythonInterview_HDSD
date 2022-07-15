


num = int(input("Enter number = "))
temp = num
reverse = 0 # i dun have reverse variable 
while num != 0 :  # my previous code while True: infinite loop
    remainder  = num%10
    reverse = reverse*10 + remainder
    num = num//10
    
print("Reverse Number = ", reverse)
# Ex original number 1234321 
# Their reverse number is 1234321
# Then if 1234321 = 1234321 is True

if temp == reverse: # or we can write num == reverse   
    print("Yes True")
else:
    print("Not palindrome")

    


