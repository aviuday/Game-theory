# Python program for the above approach
import dlib
import sys, os

def minCost(arr):

	# Call the max_cost_assignment() function
	# and store the assignment
	assignment = dlib.max_cost_assignment(arr)
	dict = {}
	for i in range(len(assignment)):
		dict[str(i)] = assignment[i]

	return dict



# Driver Code

# Given 2D array
# arr = dlib.matrix([[50,45,44,43], [50,45,44,43], [20,15,10,5], [20,15,10,5]])

# Function Call
# minCost(arr)
