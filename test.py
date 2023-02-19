# initializing string
test_string = "There are 12 apples for 4 persons"
test_string = "1-hour"
 
# printing original string
print("The original string : " + test_string)
 
# # using List comprehension + isdigit() +split()
# # getting numbers from string
# res = [int(i) for i in test_string.split() if i.isdigit()]
# # print result
# print("The numbers list is : " + str(res))

# using List comprehension + isdigit() +split()
# getting numbers from string
res = [int(i) for i in test_string if i.isdigit()]
# print result
print("The numbers list is : " + str(res))





# getting numbers from string
res = []
x=test_string.split()
for i in x:
    if i.isnumeric():
        res.append(int(i))
 
# print result
print("The numbers list is : " + str(res))