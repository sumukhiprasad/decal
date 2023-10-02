
# Let's start with an empty list:

fruits = []

#Next, let's add the following fruits to the list: 'apple', 'banana', and 'kiwi'.

fruits.append('apple')
fruits.append('banana')
fruits.append('kiwi')

#Print the second element in the list (which index would that be?)

print(fruits[1])

#Now add another 'banana' to the end of the list, and replace the first one with 'cherry'.
#See if you can do this without actually typing out 'banana' in your code.

fruits.append(fruits[1])
fruits[1] = 'cherry' #?? what is this doing? and what would insert do
print(fruits)

#Sort the list in alphabetical order (see built in methods)

fruits.sort()
print(fruits)

#Print the length of fruits

print(len(fruits))



#
#SECOND DEMO

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Slice the list to include only the integers from 2 to 9 (inclusive) and print its length.

print(len((nums[1:9]))) #my way

nums = nums[1:9]
print(len(nums))


#Now create a new list with all of the odd numbers in nums in decreasing order

reversed_odd = nums[::-2] #not inputting a start and end means that we span the entirety of the list... otherwise we could've done [9:1:-2]... If we did [1:9:-2], it wouldn't work bc it would go 1 down to the negatives in -2 intervals
print(reversed_odd)

# Creating two sample lists with different types of elements

list1 = [1,2,3]
list2 = ['a','b','c']

# Concatenating lists using the '+' operator

list3 = list1 + list2

# Printing the concatenated list

print(list3)
print(type(list3[4]))

# Creating another sample list

list4 = list1.append(list2)
print(list4)

# Concatenating lists using the 'extend()' method



# Printing the updated list1 after concatenation using 'extend()'




