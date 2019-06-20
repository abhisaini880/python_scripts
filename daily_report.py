# Script to record the daily tasks time and send report

#!/usr/bin/python3.7

# Import Libraries
import datetime
import time
import os

##### Class and Functions

class task_control:
	""" task_control class is used for manupulating the task like add task , delete task etc."""	
	def __init__(self, task_details):
		self.task_details = task_details

	def add_task(self):
		"""Function to add task and start time in list"""
		key = self.task_details
		task_list.setdefault(key, [])
		task_list[key].append(time.time())
	
	def stop_task(self):
		"""Function to record stop time for the task"""
		a[key].append(time.time())
	

class Switcher:
	"""Switcher is used for selecting the fuctions from task_control class based on user's input."""

	def __init__(self, argument, tk):
		self.argument = argument
		self.tk = tk
		self.tc = task_control(self.tk)

	def sw_func(self):
		"""Calling functions based on argument passed """
        # Get the function from switcher dictionary
		method_name = 'case_' + str(self.argument)
		func = getattr(self, method_name, "Invalid")
        # Call the method as we return it
		return func()
 
	def case_1(self):
		# call the add_task method in task_control
		return self.tc.add_task()
 
	def case_2(self):
		# call the stop_task method in task_control
		return self.tc.stop_task()

	def case_6(self):
		print("mail sent")
		exit
		
######


# Clear screen
os.system('clear')

# Print Today date
today=datetime.datetime.now()
print(f"############ Daily Report {today.strftime('%Y-%m-%d')} ################\n\n")

# Print Options to choose from
print("Choose from the Following \n\n 1. ADD Task \t\t 2. Delete Task \t\t 3. Start Task \n\n 4. List Tasks \t\t 5. Stop Task \t\t\t 6. Finish Report")

# Task list initiation
task_list = {}

while(True):
	# Taking input from user
	option, task = input().split(',')

	if (int(option) > 6):
		print("Invalid option")
	else:
		# Object creation for Switcher class
		switch = Switcher(option, task)
		# calling function for choosing the task to perform
		switch.sw_func()

		print(task_list)