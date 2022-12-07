#Introduction list

mylist = [];
print(mylist);
print(type(mylist))


int_list = [34 ,50, 70, 43]
print(int_list);

float_list = [3.89,90.87,5.67]
print(float_list);

string_list = ["hello","python","Think"]
print(string_list)

#check data type  follwing print(type(-- ))


mixed_list= ["hello", 9.08, 89 ]
print(type(mixed_list))


#How to chek data

all_list =["Think",5.78,9]
print(type(all_list[0]))
print(type(all_list[1]))
print(type(all_list[2]))

# what is multidimensional list & 2d and 3d ;

mul_list =[["I love python"],["Every think will"]]   # thats call 2d
print(mul_list)

mult_list =[["I love"],["Every"],[9033]]  #That's call 3d
print(mult_list)


# List Item Access
My_list = ["Hello",40,4.345,"Python"]
print(My_list[0])
print(My_list[1])
print(My_list[2])
print(My_list[3])


# list slicing

slicing_list  = ["Hello", "Think",  "willbe", "there are",  "Abourt",  "Every",   "Think",  "will",  "thio"]
#                 0          1          2            3            4       5          6         7       8

print(slicing_list[:])  # start :end
print(slicing_list[2:8])  # n-1
print(slicing_list[0:7])  # n-1
print(slicing_list[1:6])  # n-1

# Determin the length using len() Function

print(len(slicing_list))

Det =[]
print(len(Det))

# How to update list

MYL_list = ["Hello",78,8.974]
print("Initial list", MYL_list)

MYL_list[1] = "Think";
print("update",MYL_list)


# Add new items in list

#append(), Insert(), extend()
#manual
MT_list =[10,"python","Sun", 45.87]
print("Initial list:",MT_list)

# how to add new items in list  = Buit in functions [ Append(),Insert(), extend() ] # Manual = [       ]

#use append()
Ap_list = [50,"Hello","Love python",99.01]
Ap_list.append("I Think well")
print("Update :",Ap_list)

# use Insert() # index, # item

IN_list =[23,"Every","Think",11.3,"eee"]
IN_list.insert(3,"well be ok")
print('update::', IN_list)

#use Extend()

Ex_list1 =["hello",20,"Brother"]
Ex_list2 =["How are you"]
Ex_list1.extend(Ex_list2)
print( "Update-2:",  Ex_list1)