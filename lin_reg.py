import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# function name: least_sq
# inputs: file_name- name of the csv file 
# output: m(slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY! return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
# assumptions: The csv file will always have headers in the order of: x, y
def least_sq(file_name):
	pass


# function name: mat_least_sq
# inputs: file_name- name of the csv file 
# output: m (slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY! return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!
# assumptions: The csv file will always have headers in the order of: x, y
def mat_least_sq(file_name):
	pass


# function name: plot_reg
# inputs: mat - file_name- name of the csv file
		# using_matrix: True if you are plotting the linear equation from mat_least_Sq
		# 				False if you are plotting the linear equation from least_sq
# output: NA
# task: given file_name, compute the linear equation using least_sq or mat_least_sq and graph results
	#	your graph should have the following: labeled x and y axes, title, legend
# assumptions: The csv file will always have headers in the order of: x, y
def plot_reg(file_name, using_matrix):
	pass



######## TEST CASES ########
csv_file = "data.csv"

m1, b1 = least_sq(csv_file)
print("Slope using algebraic least squares:", m1)
print("y-intercept using algebraic least squares:", b1)
print()

m2, b2 = mat_least_sq(csv_file)
print("Slope using linear algebra least squares:", m2)
print("y-intercept using linear algebra least squares:", b2)

plot_reg(csv_file, True)

plot_reg(csv_file, False)

