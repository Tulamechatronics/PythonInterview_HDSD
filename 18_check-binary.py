

# input 10001 yes binary
# input 1110002 false
# input 672 false 

num = int(input("Enter number = "))
#temp = num
#reverse = 0 
while num != 0 : 
    remainder  = num%10
    if remainder!=0 and remainder!=1:
        print("Number is not binary")
    num = num//10
    if (num==0):
        print("Number is binary representation")
    
