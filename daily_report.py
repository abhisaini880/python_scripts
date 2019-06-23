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
		if(self.task_details in task_list):
			print("Task already exists")
		else:
			key = self.task_details
			task_list.setdefault(self.task_details, [])
			task_list[key].append(time.time())

	def del_task(self):
		""" Function to delete task if exists """
		if(self.task_details in task_list):
			del task_list[self.task_details]
			print(f" {self.task_details} Task deleted")
		else:
			print("Task do not exists")

	def start_task(self):
		""" Function to create again start the time for task and create new task if do not exists"""
		if(self.task_details in task_list):
			key = self.task_details
			task_list.setdefault(key, [])
			task_list[key][0] = time.time()
			task_list[key][1] = 0
		else:
			print("Task do not exists ... \n Adding new task")
			self.add_task()
	
	def stop_task(self):
		"""Function to record stop time for the task"""
		if(self.task_details in task_list):
			key = self.task_details
			if(len(task_list[key]) > 1): # Condition to check if the task is stopped before
				if(task_list[key][1] == 0):# condition to check if the task has been rstarted
					task_list.setdefault(key, [])
					task_list[key][1] = time.time()
					task_list[key][2] += (task_list[key][1] - task_list[key][0]) /60 # Time recorded in minutes for hours use 3600
				else:
					print("Task is not running . Please start the task again")
			else: # For stopping the task first time
				task_list.setdefault(self.task_details, [])
				task_list[key].append(time.time())
				elapsed_time = (task_list[key][1] - task_list[key][0]) /60
				task_list[key].append(elapsed_time)
				print(elapsed_time)
		else:
			print("Task do not exists")

	def show_list(self):
		""" Function to show all task list"""
		print("\n task --> start time || end time || time in minutes\n")
		for task,time in task_list.items():
			print(f"{task} ---> {time}\n")
	
	def finish_list(self):
		pass

class Switcher:
	"""Switcher is used for selecting the fuctions from task_control class based on user's input."""

	def __init__(self, argument, tk = 'default'):
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
		# call the del_task method in task_control
 		return self.tc.del_task()

	def case_3(self):
 		return self.tc.start_task()

	def case_4(self):
		# call the stop_task method in task_control
		return self.tc.stop_task()

	def case_5(self):
		return self.tc.show_list()	
	
	def case_6(self):
		print("mail sent")
		exit
		
######


# Clear screen
os.system('clear')

# Print Today date
today=datetime.datetime.now()
print(f"####################################################### Daily Report {today.strftime('%Y-%m-%d')} ######################################################################\n\n")

# Print Options to choose from
print("Choose from the Following \n\n 1. ADD Task \t\t 2. Delete Task \t\t 3. Start Task \n\n 4. Stop Task \t\t 5. List Tasks \t\t\t 6. Finish Report \n")
print("######################################################################################################################################################")
# Task list initiation
task_list = {}

while(True):

	# Try block for tasking inputs
	try:
		# Taking input from user
		options = list(input().strip().split(','))

		if (int(options[0]) > 6):
			print("Invalid option \n Kinldy provide valid option ")
		elif (int(options[0]) <= 4):
			# Object creation for Switcher class
			switch = Switcher(options[0], options[1])
			# calling function for choosing the task to perform
			switch.sw_func()
		else :
			# Object creation for Switcher class
			switch = Switcher(options[0])
			# calling function for choosing the task to perform
			switch.sw_func()

	except Exception :
		print("kindly provide the valid number of arguments")		
