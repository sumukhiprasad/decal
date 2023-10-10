###Question 1
def find_power_of_number(x,y):
   power_of_number = x**y # simple and straightforward eqn for finding the power of a number
   return power_of_number
number = find_power_of_number(3,4) # I can add this line and the one below it when I want the python file to automatically run when it opens rather than calling the function in the terminal.
print(number) # This will run anytime the python file is called in the terminal to run because it is outside of the function... The other alternative is to call the function in the terminal for it to run.

###Question 2
def min_and_max(list1): # passing into this function is an iterable object (which is any tuple, string, or list) which is why you must enter an input in either a tuple, string, or list format
    minimum = min(list1) # built-in python function
    maximum = max(list1) # built-in python function
    return minimum, maximum

###Question 3
def is_leap_year(x): 
   if x % 4 == 0: # leap years are years that are divisible by 4 and not 100 unless it is divisible by 400
      if x % 400 == 0: # first condition is met so function will check this condition
         if x % 100 == 0: # first and second conditions are met so function will now check this condition
            print("True") # it is a leap year if the above conditions are met
      elif x % 100 != 0: # this is another condition that results in a given output if the input year is not divisible by 100
         print("True") # output for when this other above option runs
      else: # another option
         print("False") # another option output
   else:
      print("False") # when the integer doesn't satisfy any of the above conditions, it will run this line. 
   return 

###Question 4
def bmi(w,h):
   print(w/h**2) # simple and straightforward equation
   return

###Question 5
def rotate_digits(x):
   m = 0 # this will be used later in the for-loop to update m as the loop runs through each digit. This rotating digits will be stored in this variable. This will be printed to show the final value after the digits have been rotated.
   count = 0 # this will initialize the while-loop to count the number of digits in the user input integer. This variable will update with every digit that is identified.
   first_number = x % 10 # this gives us the remainder after the value is divided by 10. So 123/10 will give a remainder of 3 which will be stored in this variable. This will be used in the future to move the last digit to the front of the user input, so it becomes the first number of the new value.;
   last_numbers = x // 10 # this variable performs floor division, which means that it provides the integer value part of a number and not the decimals. It rounds the result of a division problem down to it's nearest whole number.
   input = x # i added this to the code so that the input variable changes and not the user input x.
   while (input>0): # this while-loop is used to count the number of digits in the user input integer... this value will be used to run the for-loop that will update the m value as the for-loop runs or as the digits are being rotated.
      count = count + 1 # this will add 1 incrementally as the while loop runs so that the number of digits is updated accordingly.
      input = input//10 # this will divide the new input value by 10 so we reduce teh value each time by a factor of 10 to note that one digit or placeholder is accounted for.
   for i in range(0,count): # we did the whole while loop above to find count for the reason that we needed this for-loop to run from a range of 0 to count (one loop runs for index 0 and another loop runs for the first index and so on and so forth - so this loop will run a total of 'count-1' times) and update the variable m as the digits are being rotated.
      if m == 0: # this if statement is run to update m as the first index of the range (since m only equals 0 once, this if statement will never run again).
         m = first_number # this sets m to be the first_number variable we had created earlier. This will make the last number of the digit that was inputted now become the first number in the m variable (which is what we want since we want the last digit of the user input integer to move to the very front position)
      else:
         m = m*10 # this line will run each time a digit is identified until the last digit is being looped and will multiply the variable m by 10. So that we can just stick the last_numbers variable at the end of the m variable (the variable in which the rotated digits are being stored) by adding it to the existing m variable.
   m = m + last_numbers # must be placed outside of for-loop, otherwise this line will run after each time the loop runs for the given index/element of that range/set.We don't want that happening because then m will be increasing by last_numbers each time the loop completes and this number will be multiplied by 10 - which will give us the wrong answer. You only want this line to happen once - at the very end of the code. 
   print(int(m)) # prints the final m variable after the digits have been rotated.
   #print(count) # I had added this to check if my count variable was updating accordingly.
   #print(first_number)
   #print(last_numbers)
   return


#Question 5
#def rotate_digits(x):
  # first_number = x % 10 
  # last_numbers = x // 10
  # print(x-x+first_number*10+)

#int res = 0, tmp, number ,lastDigit ;

    # scanf ("%d", &number);
     #tmp = number;
     #lastDigit = number % 10;
     #while(tmp /=10)
      #  lastDigit =  lastDigit * 10 ;

     #res =  lastDigit  + number/10 ;


###Question 6

#below are two ways of calculating the maximum value of a list, one using boolean as the initializer and the other not

#option 1
def max_for_loop(list1):
   first = True # in order for the for-loop to read through each index of the list, I need to initialize the first index of the list using an if statement. Otherwise, it won't start the comparison process. So i initialize using this line so that the line can be turned False after the first element of the list is read, and then the code can run through the latter part of the code. 
   for i in list1: # running a for-loop for any iterable object inputted by the user (likely will be a list)
      if first: # creates the condition for the first element to be read in by the for-loop
         m = i # updates m to be the first element
         first = False # stops this if-statement from running again
      if i > m: # if the current index is larger than m (which was the indexed element before it), then this statement will run.
         m = i # updates m to be the index being analyzed at this time if the current inded is larger than m (the largest value up until this current index was being analyzed)
   print(m) # prints the final m value which is the largest value out of the list
   return

#option 2
def max_for_loop2(list1): # this code runs the same way the previous code does although it initializes the first index of the list to be read using m = 0 rather than a boolean
   m = 0
   for i in list1:
      if m == 0:
         m = i
      if i > m:
         m = i
   print(m)
   return

#calculating minimum value using for loop
def min_for_loop(list1): # look at above comments for detailed explanations... it runs the same way the previous loops run except it is looking for a minimum rather than a maximum value.
   m = 0
   for i in list1:
      if m == 0:
         m = i
      if i < m:
         m = i
   print(m)
   return

#calculating maximum using while loop
def max_while_loop(list1): # I want the while loop to keep going through the list until it finds the largest value.
   #so then this means that I will keep comparing each value to the before it and keep updating the max value so that it shows me the most up-to-date value for maximum until it finds the max of the entire list
   #so the stopping point is when the max value has been found
   i = 0 # initializing with i = 0 to run through each index of the list
   max_value = list1[i] # sets the current max value as the value at the 0th index of the list
   while i < len(list1): # as long as i is less than the total number of elements in the list, this while loop will run
      if list1[i] > max_value:
         max_value = list1[i] # if the current index's value is greater than the value at index 0 (indicated by the previously initialized max_value variable), then we instruct computer to set the max_value to the value at the index we are looking at. And then the loop is completed for the if statement and then the next element will be analyzed.
      i = i + 1 # this needs to be placed outside of the if statement because otherwise the code will not actually run through each element in the list... this is because if the if statement has the i = i + 1 within it (which is the part that iterates through each element in a list), then the i = i + 1 will only run if it satisfies that if statement's condition. Otherwise, if the condition is not met, the code will just stop and not ever print because it is constantly in the if statement loop and won't ever get out of the loop to eventually print the "print(max_value)" part since the while loop condition is not being satisfied (since we are not passing through each element in the list if we are stuck in the if statement loop).
   print(max_value)
   return
   
#calculating minimum using while loop
def min_while_loop(list1): # I want the while loop to keep going through the list until it finds the smallest value.
   #so then this means that I will keep comparing each value to the before it and keep updating the min value so that it shows me the most up-to-date value for minimum until it finds the min of the entire list
   #so the stopping point is when the min value has been found
   i = 0 # initializing with i = 0 to run through each index of the list
   min_value = list1[i] # sets the current min value as the value at the 0th index of the list
   while i < len(list1): # as long as i is less than the total number of elements in the list, this while loop will run
      if list1[i] < min_value:
         min_value = list1[i] # if the current index's value is less than the value at index 0 (indicated by the previously initialized max_value variable), then we instruct computer to set the min_value to the value at the index we are looking at. And then the loop is completed for the if statement and then the next element will be analyzed.
      i = i + 1 # this needs to be placed outside of the if statement because otherwise the code will not actually run through each element in the inputted list... this is because if the if statement has the i = i + 1 within it (which is the part that iterates through each element in a list), then the i = i + 1 will only run if it satisfies that if statement's condition. Otherwise, if the condition is not met, the code will just stop and not ever print because it is constantly in the if statement loop and won't ever get out of the loop to eventually print the "print(max_value)" part since the while loop condition is not being satisfied (since we are not passing through each element in the list if we are stuck in the if statement loop).
   print(min_value)
   return

###Problem 7
def vowel_count(list1):
   count = 0 # initializes the count so it increases in value as the loop runs and a vowel is identified.
   for i in list1: # for when the index runs through any iterable object - in this case, the object will be a string.
      if i in ("a","e","i","o","u","A","E","I","O","U"): # if I am going to use OR operator to separate the vowels, I must write i == "a" or i == "e" or i == "i"... etc.
         count += 1 # count increases by 1 every time one of the above vowels is identified.
   print(count) # provides the number of vowel in a given string input
   return

#Problem 8
#the following code cannot work because the problem asks for a integer input and not a list input... and this code is designed specifically for an iteratable object to be inputted by the user. This code won't run for an integer user input because a for-loop which only reads in iteratable objects such as lists, tuples, and strings. An integer is not an iteratable object, so the for-loop won't run. This code will only work if I convert the integer user input into a string so that the for-loop can read in a string and not an integer.
# def digital_root(list1): 
#    m = 0
#    for i in list1:
#       if i == 0:
#          m = m + i
#       else:
#          m = m + i
#    print(m)
#    return

###Problem 8
def digital_root(list1): 
   string = str(list1) #the computer can only create a for-loop for an iterable object such as a list or range. However, I want the input of the function on the user end to be an integer. Thus, I have to convert the user's integer input into a string in order for the for-loop to run later on (since a for-loop only runs on strings (which are lists), lists, or ranges)
   m = True # m equals 0 .... i scratched that because i realized that if "000" is entered, only the first if statement will run over and over again... anyways, this line is written because it will initialize the for-loop for the first index of the list or range. Otherwise, there is no way for the for-loop to iterate through each object in the list - it will stay in a never-ending cycle of not even running the rest of the code for the latter elements since nothing is being run for the first index. 
   for i in string: #I am going to create a for-loop to run i through each index of the string variable (which is now an iterable object after the str() function was applied)
      if m == True: # condition for solely the first index of the string to be initialized (the variable for which we had defined earlier)
         m = m + int(i) # updates the m variable to be the first index of the list - this if statement will never run again since m won't ever be true again since the last part of this section makes m equal to false.
         m == False # makes m false so this section of the code will never run again after the first index of the string is read... this is because m is forever false after this loop runs
      else:
         m = m + int(i) # updates m accordingly after the first index of the string is read
   print(int(m)) # prints m as an integer in case it was read as a string before... which it wasn't, but I just wanted to make sure
   return

