# print("Hellow World")
# name="vinay"
# print(name)
# print(name.upper())
# print(name.capitalize())
# print(name.__len__())
# print(len(name))
# my_list=['apple', 'banana', 'mango']
# print(my_list)
# my_list.append('kiwi')
# print(my_list)
# my_list[0]='orange'
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.remove('mango')
# print(my_list)
# print(my_list.index('banana'))
# print(my_list[-1])
# my_set1={1,2,3,4,5}
# my_set2={2,4,6,7}
# print(my_set1.intersection(my_set2))

# my_dict={'key1':'value1', 'key2':'value2', 'key3':'value3'}
# print(my_dict['key1'])
# my_dict['key4']=['value4']
# print(my_dict)
# my_dict['key1']='value1 is modified'
# print(my_dict)
# print(my_dict.items())
# print(my_dict.keys())

# num = int(input("Enter a number: "))
# if num < 0:
#     print(num, "is a negative number")
# elif num%2 ==0:
#     print(num, "ia an even number")
# else:
#     print(num, "is an odd number")

num = (input("Enter a number: "))
if isinstance(num,str):
    print("warning: please enter a valid number")
elif int(num) < 0:
    print(num, "is a negative number")
elif int(num)%2 ==0:
    print(num, "ia an even number")
else:
    print(num, "is an odd number")