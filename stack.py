class Stack:
	def __init__(self):
		# Initialise the stack's data attributes
		self.l=[]
		pass
	
	def push(self, item):
		# Push an item to the stack
		self.l.append(item)
		pass

	def peek(self):
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
		if(self.is_empty()):
			return "Error"
		else:
			return self.l[-1]
		pass

	def pop(self):
		# Pop an item from the stack if non-empty
		if(self.__len__()!=0):
			self.l.pop()
		pass

	def is_empty(self):
		# Return True if stack is empty, False otherwise
		return (self.__len__()==0)
		pass

	def __str__(self):
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
		for i in range(self.__len__(),0,-1):
			print(str(self.peek()),end=" ")
		print()	
		pass

	def __len__(self):
		# Return current number of elements in the stack
		return len(self.l)
		pass