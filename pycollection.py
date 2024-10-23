"""
list
tuple
set
dictionary
"""

# how to create a list
list_of_student=["Isreal", "malik","malik", "John Wick","Bankole","Taiwo","John Praise"]
list_of_student2=list(("Isreal", "malik", "John Wick","Bankole","Taiwo","John Praise"))
# list_of_student.append("Tikristi")
# print(list_of_student)
# print(len(list_of_student))
# print(type(list_of_student))
# print(list_of_student2)
# print(type(list_of_student2))

# names=[]
# for each in range(1, 4):
#     user=input("enter name>>> ")
#     names.append(user)
# print(names)
# list_of_student.clear()
# count_itm=list_of_student.count('malik')
# print(list_of_student.count('malik'))
# print(count_itm)

# list_of_student.extend(('tolu','bola', 'kike'))
# print(list_of_student)

# names=[]
# all_name=[]
# for each in range(1, 3):
#     user=input("enter name>>> ")
#     age=input("enter age>>> ")
#     address=input("enter address>>> ")
#     # names.append(user)
#     all_name.extend((user,age,address))
#     print(all_name[1])
# print(all_name)

# list_of_student.insert(0, "saheed")
# print(list_of_student)







# user_name=[]
# for each in range(1,3):
#     user_names=input("enter the names")
#     location("enter the location")
#     gmail=("enter the gmail")
#     password=("enter the password")



# for each in range(1,6):
# user_name=input("Enter user_name")
# for each2 in range(1,6):
# password=input("enter password")
# print("""
#                                 WELCOME TO JP GROUPS OF SCHOOL
#             SELECT
#             1. REGISTER
#             2. exit
#         """)
# user_option=input("enter an option>>> ")
# students=[]
# all_students=[]
# if user_option=="1":
#     for each in range(1,3):
#         name=input("enter name>>> ")
#         username=input("enter username>>> ")
#         passwd=input("enter password>>> ")
#         students.extend((name,username,passwd))
#     print("registration successful")
#     print('kindly login'.center(100))
#     name=input("enter username>>> ")
#     username=input("enter password>>> ")
#     if name and username not in students:
#         print('you have to register first....')
#     else:
#         print("you are successfully login in")

# else:
#     print("invalid input")



# TUPLE
'''
how to declare a tuple
accessing it
it method
unpacking
looping a tuple
join tuple (using + or * )
'''
# TUPLE
# Tuple: A tuple is a collection that is ordered but not changeable. A tuple is created using
#  braces i.e () or tuple() constructor




# items=("laptop","phone","wahing machine","tv","pressing iron")
items=tuple(("mango", 'sunday', "mango",'ikeja','favorite color'))
# product=("gucci bag","D&G","Nike")
# print(type(items))
names = ("Shade", "energy", "magnet", "Chale", "Energy", ('energy101','cashew','Babatunde'),('Olawale','orange','Ekiti') )
# list_of_items=(('rice', 'mango','tolu'),('maize', 'cherry','Azeez'),('cowpea','cashew','Babatunde'))
# print(items[::2])      #slicing
# print(names[6][0:1])    # accessing nested tuple
# # print(len(names))
# # names[2]='Olawale'
# new_name=list(names)
# print(new_name)
# new_name[2]='Olawale'
# print(new_name)
# name=tuple(new_name)
# print(names)


# print(type(name))
name2 = tuple(('binpe','tolani',10, 'oyo','ikeja'))

# print(type(name2))
# print(name2)
# print(name[3])
# print(name[1:4])
# print(name2[-3])
# print(name2[-4:-1])

# method applicable on tuple
count_item1=items.count('mango')
count_item=items.index("sunday")
print(count_item1)
print(count_item)
# Unpacking values of a tuple
# item = ("yam", "Sunday", "Lagos", 45,'yam')
# food, name, location, score=item
# print(type(food))


list_of_items=(('rice', 'mango','tolu','milk'),('maize', 'cherry','Azeez','milo'),('yam','cashew','Babatunde','coco'),  ('beans', 'orange','Azeez','milo'))
# tuple1,tuple2, *theRemainingItems=list_of_items
# print(tuple2[2])
# for food,fruit,_,_ in list_of_items:
#     food_fruit=f'{food}:{fruit}'
#     print(food_fruit)
# print(theRemainingItems)
# cereal, *others =list_of_items
# print(cereal)
# crop=[]
# # for food, _, _, _ in list_of_items:
#     crop.append(food)
#     crop.append('beans')
# print(crop, 'our food ')
# print(cereal[0])
(food, fruit, name, brevages) = list_of_items  #unpacking each element into new variables
# print(name)
# (food, *others, age) = item      #this '*' means all
# print(others)
# (food, *others) = item
# print(food)
# print(others)














