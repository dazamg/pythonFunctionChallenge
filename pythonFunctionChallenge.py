#1
# def sum_to(n):
#     sum = 0
#     for i in range(n + 1):
#         sum += i
#     return sum

# print(sum_to(6))
# print(sum_to(10))



#2
# def largest(list):
#     largest_num = 0
#     for item in list:
#         if item > largest_num:
#             largest_num = item
#     return largest_num

# print(largest([10, 4, 2, 231, 91, 54]))
# print(largest([1,2,3,4,0]))



#3 
# I don't understand or knew how to do this one, i look at the solution. 
# i need to practise it more 











#4 
def product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

print(product(6))