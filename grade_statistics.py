#!/usr/bin/python

"""
Grade_statistics.py

Prompt use for grades (0-100 with input validation)
and compute the sum, average, minimum, and print the horizontal histogram.

An example to illustrate basic Python syntaxes and constructs, such as block 
indentation, conditional, for-loop, while-loop, input/output, list and function.

"""

# Define all the functions before using them

# function to calculate the sum of the given list
def my_sum(lst):
	sum = 0
	for grade in lst:
		sum += grade
	return sum


# function to calculate the average of the given list
def my_average(lst):
	average = my_sum(lst)/len(lst)

	return average


# function to calculate the minimum of the given list
def my_min(lst):
	min = lst[0]

	for grade in lst:
		if grade < min:
			min = grade

	return min


# function to calcute the horizontal histogram
def print_histogram(lst):
	# Create a list of 10 bins to hold grades of 0-9, 10-19, 20-29,.... 90-100
	# bins[0] to bins[8] has 10 items, but bins[9] has 11 items

	bins = [0] * 10 # use reetition operator (*) to create a list of 10 zeros
	print bins

	# populate the histpgram bins from the grades in the given list
	for grade in lst:
		if grade == 100:    # special case
			bins[9] += 1
		else:
			bins[grade//10] += 1  # Use // for integer divide to get a truncated int

	# print histogram
	# 2D pattern: rows are bins, columns are value of that particular bin in stars
	for row in range(len(bins)):  # [0,1,2,3....len(bins) -1 ] 
		# print row header
		if row == 9:   # Special case
			print '{:3d}-{:<3d}: '.format(90, 100),  # Formatted output (new style), no newline
		else:
			print '{:3d}-{:<3d}: '.format(row*10, row*10+9),  # Formatted output, no newline

		# Print one start per count
		for col in range(bins[row]):
			print '*' , # no newline
			print '\n'
			#print() # newline
			# alternatively, use strs, repitition operator (*) to create the output string
			# print('*'*bins[row])





def main():
	""" The main function """
	# Create an initial empty list for grades to recieve from input
	grade_list = []

	# Read grades with input validation
	grade = int(input('Enter a grade between 0 and 100 (or -1 to end: '))
	while grade != -1:
		# Python supports this comparision syntax
		if 0 <= grade <= 100:
			grade_list.append(grade)
		else:
			print('invalid grade, try again...')
		grade = int(input('Enter a grade between 0 and 100 (or -1 to end: '))

	# call function and input results
	print('-----------------------')
	print('The list is: ', grade_list)
	print('The minimum is: ', my_min(grade_list))
	print('The minimum using built-in function is: ', min(grade_list))
	print('The sum is: ', my_sum(grade_list))
	print('The sum using built-in function is: ', sum(grade_list))
	print('The average is: %.2f' %my_average(grade_list))
	print('The average is: {:.2f}'.format(my_average(grade_list)))
	print('------------------------')
	print_histogram(grade_list)


# Run the main function
if __name__ == '__main__':
	main()