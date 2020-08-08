#!/usr/bin/python

"""
number_guess - Number Guess Game
This example illustrates while-loop with boolean flag, nested-if, and random module.

"""

import random # using random.randit() to generate random integers

# set up a secret number between 0 and 99
secret_number = random.randint(0, 100) # return a random int between [0, 100]
trial_number = 0 # number of trials
done = False     # bool flag for loop control

while not done:
	trial_number += 1
	number_in = int(input('Enter your guess (between 0 and 100): ' ))
	if number_in is secret_number:
		print('Congratulations!')
		print('You got it in {} trials.'.format(trial_number))
		done = True
	elif number_in < secret_number:
		print('Try higher number...')
	else:
		print('Try lower number...')