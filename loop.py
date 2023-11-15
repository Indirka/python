# [1,2,3,4,5,6,7,8,9,10] 
# for i in range(1,14,4):
#     print(i)

# for letter in 'INdira':
#   print(letter)

# print('Using a list')
# for y in ['red', 'white', 'orange', 'blue', 'pink']:
#    print(y)

# print('Break Keyword Example')
# for i in [0, 2, 4, 8, 10, 12, 14]:
#     if  i == 3:
#         break
#     print(i)

# for x in range(9):
#     print("1")


# for z in range(20, -20, -5):
#     print(z)

# for x in "apple":
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if  x == "banana":
#         break

# for x in range(6):
#   if x == 4: break
#   print(x)
# else:
#   print("Finally finished!")

# abc = ["red", "big", "tasty"]
# cbs = ["apple", "banana", "cherry"]
# for x in abc:
#     for y in cbs:
#         print(x, y)



# for x in range(7):
#     if x == 0 or x == 6:
#         print("*")
#     elif x == 1 or x == 5:
#         print("**")
#     elif x == 2 or x == 3:
#         print("***")
#     else:
#         print("****")

    # Additional conditional statements for amount_loaded
# amount_loaded = x * 25
# if amount_loaded == 25:
#     print("1/4 of the way there")
# elif amount_loaded == 50:
#     print("1/2 of the way there")
# elif amount_loaded == 75:
#     print("3/4 of the way there")
# elif amount_loaded == 100:
#     print("Loading complete!")

exp = [2345, 2341, 2144, 2674, 3000]
total = 0
for i in range(len(exp)):  
    print('Month:', (i+1), 'Expense:', exp[i])
    total = total + exp[i]
print('Total expense is :',total)    