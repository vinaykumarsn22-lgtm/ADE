# def add_numbers():
#     return 10+20
# print(add_numbers())

# def add_numbers(a, b):
#     return(a+b)
# print(add_numbers(5, 8))

# def add_numbers(a, b=50):
#     return(a+b)
# print(add_numbers(20, 20))

# def add_numbers(a, b=50):
#     return(a+b)
# print(add_numbers(20))

# def add_numbers(a=50, b):
#     return(a+b)
# print(add_numbers(20))

# def add_numbers(a=10, b=50):
#     return(a+b)
# print(add_numbers(20, 20))

# def add_numbers(a=20, b=50):
#     return(a+b)
# print(add_numbers)


# def my_fruits(*fruits):
#     for fruit in fruits:
#         print(fruit)
# my_fruits('grapes', 'mangos', 'banana', 'litchi')
# my_fruits('orange','apple')

# def is_even(num:int) -> bool:
#     return num%2==0
# print(is_even(20))
# print(is_even(23))

# lambda function| anonymous function

# is_even = lambda num: num%2==0
# print(is_even(10))

# filter & map

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = list(filter(lambda num:num%2==0, nums))
# print(even_nums)
    
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_nums = list(map(lambda num:num**2, nums))
# print(squared_nums)

# def outer_function(abc):
#     def inner_function():
#         print(abc)
#     inner_function()

# outer_function('Hello, Good Morning')

# li = [3, 2, 4, 8, 5]
# li.sort()
# li.reverse()
# print(li)

# data = [
#     (100, 'Lokesh', 40000),
#     (101, 'Srinath', 25000),
#     (102, 'Gaganh', 50000)
# ]

# sorted_data = sorted(data, key=lambda x:x[2])
# print(sorted_data)

# word = ['apple', 'mango', 'orange', 'banana', 'umbrella']
# word_cnt = len(list(filter(lambda w: w[0] in 'aeiou', word)))
# print(word_cnt)

# word = ['apple', 'mango', 'orange', 'banana', 'umbrella', 'Airport', 'Omega']
# word_cnt = len(list(filter(lambda w: w[0].lower() in 'aeiou', word)))
# print(word_cnt)

# 1. Minimum 8 characters should be there
# 2. Atleast one digit should be there
# 3. Atleast one uppercase should be there

def valid_password(pwd):
    if len(pwd) < 8:
        return False
    has_digit = any(c.isdigit() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    return has_digit and has_upper

print(valid_password('Qwerty32'))
print(valid_password('Qwerty'))
print(valid_password('werty32'))