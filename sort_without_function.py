

# [9,2,5,7,19] -> [2,5,7,9,19]
number_list = [100,55,70,80,-100,8.5,13,2022,-2025]

# for n in range (0, len(number_list)):
#     for m in range (n+1, len(number_list)):
#         if number_list[n] > number_list[m]:
#            number_list[n], number_list[m] = number_list[m], number_list[n]
# print("Small to Big = ",number_list)
        
for n in range (0, len(number_list)):
    for m in range (n+1, len(number_list)):
        if number_list[n] < number_list[m]:
           number_list[n], number_list[m] = number_list[m], number_list[n]
print("Big to Small = ",number_list)           

