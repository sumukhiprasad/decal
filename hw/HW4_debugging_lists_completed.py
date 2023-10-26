"""
HW 4: Debugging and Lists

Q1 Debugging

Throughout this homework, whenever you encounter an error, we would like you to 
explain in a comment what it was and how you fixed it. You can write all these errors 
at any place in the file.

###
Errors experienced:
1. I received an error saying that the list_2D = #COMPLETE ins invalid syntax. I just added a "#" at the beginning of the variable to comment it out. I got the same error for a couple other lines in the template. I just added a "#" to comment those out.
2. I received an error that said 'builtin_function_or_method' object is not subscriptable. To fix this error, I googled this error and found that this error occurs when there is no parenthesis associated with the method. So I got this error when I had "empty_list.append[new_element]" in the code. To fix this error, I just changed the brackets in the previous code to parenthesis as shown here: "empty_list.append(new_element)". This fixed the error. To call a method in python, parenthesis instead of brackets must be used.
3. I received an error that said that a function "list_odd_integers() is missing 1 required positional argument: 'list'" when I had written "def list_odd_integers(list1)" in the code. So it was expecting me to pass in a list input. To bypass this, I defined the function as not having any input and took out the "list1" from the parenthesis so it was empty. And then I took out the "return" towards the end of the code and replaced it with list_odd_integers() at the end of the code (not indented at all) so that the terminal would automatically call and run this function without any input.
4. I received an error that said that it cannot access local variable 'i' where it is not associated with a value when I wrote "for i in listA and i in listB:" in my code. To fix this error, I just added a for-loop for listB separately so that two separate for-loops would run, one after the other.
5. I got an error for not having quotation marks around the "?" in the following: "result_list.append(?)". I fixed this error by adding quotation marks around the question mark as such: "result_list.append("?").
6. I received an error when I tried running the file in the terminal. I have to remember to exit() out of the file running (which is indicated by ">>>". this means that we are running code within a specific file). Then, once i get to the file location/directory, I can type python -i 'file_name' (the file name being the file whose script you want to run), to run a file from the command line.
7. To submit a homework using Github, I must go on my GitBash terminal, locate the directory in which the homework is stored, and click (without quotations) "git add .", "git commit -m 'a meaningful message'", and git push


Q2: List Slicing and Striding:

Part 1: Create a variable (name it anything you want but make it descriptive!) that 
is assigned to a list with the numbers 0 to 50. You should not have to write each 
number manually.
"""
#Q2 part 1 code here:

its_peanutbutter_jelly_time = list(range(0,51)) # this creates a list of numbers 0 to 50 using the range function 
print(its_peanutbutter_jelly_time) # this prints the variable its_peanutbutter_jelly_time


"""
Part 2: Create a function that takes in a list and squares each element in the list.
"""
#Q2 part 2 code here:

def list_squares(list1): # this is definining a function that takes in any list input 
    empty_list = [] # this initializes an empty list of values
    for i in list1: # this creates a for-loop that indexes through the list input
        new_element = i**2 # this squares the indexed element for that given loop
        empty_list.append(new_element) # this adds the squared element to the previously initialized list
    print(empty_list) # this prints the list of squared values


"""
Part 3: You are given two lists: listA and listB. listA contains the integers 1 through 
10 while listB contains the integers 20 through 30. Return a single, new list containing
only the odd integers of both lists in sorted order.
"""
#Q2 part 3 code here:

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # this was provided to us
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30] # this was provided to us

def list_odd_integers(): # defines the list_odd_integers function
    new_list = [] # creates an empty list that will populate as the for-loops run depending on if the if statements are satisfied or not
    for i in listA: # loops through each element of the listA provided in the homework
        if i % 2 != 0: # if there exists any remainders after the element is divided by two, the element will be appended to the new_list list
            new_list.append(i) # this appends the new_list with the element i IF the if-statement is satisfied.
    for i in listB: # loops through each element of the listB provided in the homework. This occurs after the for-loop for listA because we want the odd numbers appended to new_list to be in sequential order. Since all the elements in listA are less than the elements in listB, we will be running the for-loop for listA first so those odd elements in listA are appended to the new_list list first.
        if i % 2 != 0: # if there exists any remainders after the element is divided by two (meaning the element is odd), the element will be appended to the new_list list.
            new_list.append(i) # this appends the new_list with the element i IF the if-statement is satisfied.
    print(new_list) # this prints new_list of odd integers after listA and listB have been looped through.
list_odd_integers() # leaving this in the code instead of calling this function in my terminal allows for the function to run within the code instead of needing to call it in the terminal. I could've easily left this line out of the code and just call the function 'list_odd_integers()' in my terminal. I just did not do that because I tend to associate calling a the function in the terminal with a user input value, which was not needed for this problem. So I just included the called function line within the code.  


"""
Q3: 2D Lists
Using nested for-loops, create and print a 5x5 2D list with the numbers from 1 to 25.
"""

# Q3 PART 1 CODE HERE
list_2D = list(range(0,25)) # this creates a list of numbers from 1 to 25

# def list_odd_integers_1_to_25(): #PRACTICE
#     list_odd_integers_1_to_25 = [] #PRACTICE
#     for i in list_2D: #PRACTICE
#         if i % 2 != 0: #PRACTICE
#             list_odd_integers_1_to_25.append(i) #PRACTICE
#     return list_odd_integers_1_to_25 #PRACTICE

#Hint: Outer loop will manage row indices, inner loop will manage column indices (or vice 
# versa).

import numpy as np # this will dictate numpy as the alias np after it is imported

empty_array = np.empty((5,5)) # this creates an empty array of 5 rows and 5 columns
integers_to_fill_matrix = 1 # this initializes this variable so that it can eventually be manipulated through the for-loop to update the values in the array

for i in range(0,5): # for any i, or row, with index 0 to 5 (this will run the i for-loop for the given index and then will run the j for-loop for the same index - so the j for-loop will run with j being 0 to 5 for the row being of index 0 and so on and so forth)
    for j in range(0,5): # for any j, or column, with index 0 to 5 
        #paths = [i,j]
        empty_array[i,j] = integers_to_fill_matrix # we will update the i row and j column (coordinate point: (i,j)) being analyzed in the for-loop with the value of the variable integers_to_fill_matrix
        integers_to_fill_matrix = integers_to_fill_matrix + 1 # this will update the integers_to_fill_matrix variable by 1 each time a specific coordinate is updated so that each coordinate is populated with values from 1 to 25, without any reoccurences
print(empty_array) # this will print the 5x5 array once all the coordinates have been populated with an integer (meaning once the for-loops have been entirely iterated through)

#print()


"""
Now with your completed list_2D, replace all multiples of 3 with '?' character and print
the resulting 2D list.
"""

# Q3 PART 2 CODE HERE
#What conditional can you use to check if numbers are multiples? I can just use the modulo operator to check if the numbers are multiples of something by making it equal to zero, so the remainder is equal to zero after dividing the integer by a certain number (making it a multiple).

result_list = [] # this creates an empty list that will be populated as the for-loop runs.
for i in list_2D: # this will run through the list of elements from 1 to 25 that we had defined earlier
    if i == 0: # if the element being analyzed in the list_2D is equal to zero, the number will be appended to the result_list (this had to be included because without this line and with the next if-statement running, the computer was placing a "?" to replace 0 in the empty list since technically it being divided by 3 has a 0 remainder and thus adding a "?" where there is a zero in list_2D)
        result_list.append(i) # this appends the result_list with the i element being analyzed at that moment
    elif i % 3 == 0: # if i divided by 3 has no remainders, the code will append the result_list with a "?"
        result_list.append("?") # this will append result_list with a "?"
    else: # the last option is that if the i element being analyzed is not evenly divisible by 3 with zero remainders, result_list will be appended with the index being analyzed in the for-loop
        result_list.append(i) # appends result_list with i (meaning that i is not an odd number and is thus not being replaced with a "?")
print(result_list) # this prints the result_list list after the respective values have populated and for-loop has ran to completion (meaning that all elements in list_2D have been looped through)

"""
Q4: More List Practice

Write a function that takes in a list and returns a copy of that list with duplicate 
values removed.
"""

def remove_duplicates(list1): # this defines the remove_duplicates function that takes in any list input
    list_duplicates_removed = [] # this initializes an empty list list_duplicates_removed
    list_to_check_duplicates = [] # this initializs an empty list list_to_check_duplicates
    for i in list1: # this creates a for-loop that runs through every element in the list1 user input
        if i not in list_to_check_duplicates: # if the index being analyzed is not in the list_to_check_duplicates list, the index will be appended to the list_duplicates_removed list and list_to_check_duplicates list. This will prevent the i element from populating on the list_duplicates_removed twice due to the nature of how the if-statement is written. Because of the condition of the if-statement, if element i is already in the list_to_check_duplicates list, the if-statement will not run and a reoccuring i will not be populated in either list again. 
            list_duplicates_removed.append(i) # this appends i into list_duplicates_removed if the if-statement condition is satisfied
            list_to_check_duplicates.append(i) # this appends i into list_to_check_duplicates if the if-statement condition is satisfied
    print(list_duplicates_removed) # this prints list_duplicates_removed after the for-loop has run to completion. This list will show a copy of the list user input with the duplicates removed.
    return # any statement or line after the return statement will not be executed and thus must be included to dictate the end of a function's code. This also allows for the function to be called in the terminal for it to be run with some user input.


#It may be helpful to create an array to test your function.
#test = [40, 10, 80, 50, 20, 60, 30]

