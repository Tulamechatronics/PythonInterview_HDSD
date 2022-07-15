


num = int(input("Enter number = "))
result = num
reverse = 0 # i dun have reverse variable 
while num != 0 :  # my previous code while True: infinite loop
    remainder  = num%10
    reverse = reverse*10 + remainder
    num = num//10
    
print("Reverse Number = ", reverse)
if result == reverse:
    print("Yes True")
else:
    print("Not palindrome")

    


