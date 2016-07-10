# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 
def item_cost(cost_of_item, state_abbreviation, tax = .05):
	""" Code to calculate item cost by adding tax

	Tax is normally 5% but in California it's 7%. If the user inputs "CA" as the state
	abbreviation, then the tax will reset to 7%. If the user doesn't enter a tax rate,
	the tax rate defaults to 5 percent (.05) 
	"""

	if state_abbreviation == "CA":
		tax = .07
	return cost_of_item + cost_of_item * tax


print item_cost(5,"CA")                  #testing function
print item_cost(10,"NV",.1)
print item_cost(10,"CA",.1)
print item_cost(100,"FL",.15)


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".
def is_berry(fruit):
	""" This function takes in a fruit name and tells you if its a berry or not.

	The fruit name is taken in as a string. If the fruit is a strawberry, cherry,
	or blackberry, then the function will return True. Otherwise, it will return False.
	"""

	fruits_selected = ["strawberry", "cherry", "blackberry"]
	fruit = fruit.lower()									#convert to lower case
	#print fruit
	if fruit in fruits_selected:
		return True
	else:
		return False

print is_berry("Cherry")									#testing function
print is_berry("OLIVE")
print is_berry("apple")

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def shipping_cost(fruit_name):
	""" this function will calculate the shipping cost depending on what type of fruit.

	If the fruit is a berry, the cost is 0, if the fruit isn't a berry, the cost is 5.
	"""

	if is_berry(fruit_name) == True:				#calling is_berry function
		#print "0"
		return "0"
	else:
		#print "5"
		return "5"

shipping_cost("Cherry")								#testing function
shipping_cost("apple")
shipping_cost("Olive")

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
def is_hometown(town_name):
	""" this function will take in a town name and tell you if there's a match

	My hometown is Miami, so it'll only return true if you key in Miami.
	"""

	if town_name == "Miami":
		return True
	else:
		return False

print is_hometown("Miami")
print is_hometown("San Francisco")
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
def full_name(first_name,last_name):
	""" ths function combined the first and last name into a string which is the full name"""

	name_combined = first_name + " " + last_name
	#print name_combined
	return name_combined


full_name("Lori", "Bard")						#testing
full_name("Junior", "Russell")
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.
def hometown_greeting(home_town,first_name,last_name):
	""" This function calls on two other functions to figure out how to greet someone

	If the person is from my hometown, I acknowledge it. If not, I ask them where 
	they are from.
	"""

	if is_hometown(home_town) == True:
		print "Hi, %s, we're from the same place!"%(full_name(first_name,last_name))
	else:
		print "Hi, %s, where are you from?"%(full_name(first_name,last_name))


hometown_greeting("Miami", "Lori", "Bard")					#testing function
hometown_greeting("San Francisco", "Dianne", "Feinstein")

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(num= 1):
	""" increment adds x to a number specified in the function An inner function, add
	adds the numbers together.
	"""
	#y=5
	x = num						 #need a value for y to call add function,randomly chose 5
	def add(y):
		return x + y
	num2 = add(y)
	return num2


#print increment(1)					#testing
#print increment(5)



	

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

y = 5
addfive = increment(5)
print addfive
y = 20
addfive = increment(5)
print addfive

	



# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def add_a_number(num,list_of_numbers):
	""" this function adds the number to the list of numbers.

	the input is a number which will be added to the end of a list of numbers (the second input is the list to add to)
	"""

	list_of_numbers.append(num)
	#print list_of_numbers
	return list_of_numbers

add_a_number(5,[5,6,7,8,9])
add_a_number(35,[1,2,3,4,5,6,7])


#####################################################################