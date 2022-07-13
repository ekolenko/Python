str_1 = input('--> ')
str_2 = input('--> ')

# count = 0
# y = 0

# for i in range(len(str_1)):
   
#     if str_1[i] == str_2[y]:
#         y += 1
#     else:
#         y = 0
    
#     if y == len(str_2):
#         count += 1
#         y = 0

# print(count)
    
i = 0
count = 0

while i > -1:
    i = str_1.find(str_2, i + 1)
    count += 1

print(count - 1)