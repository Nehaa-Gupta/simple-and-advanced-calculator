from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		"""
		Call super().__init__()
		Instantiate any additional data attributes
		"""
		super().__init__()
		self.h=[]
		self.l=[]

		pass

	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
	
		if(self.check_brackets(self.tokenize(input_expression))):
			self.h.append((input_expression,self.evaluate_list_tokens(self.tokenize(input_expression))))
			return self.evaluate_list_tokens(self.tokenize(input_expression))
		else:
			self.h.append((input_expression,"Error"))
			return "Error" 

		pass

	def tokenize(self, input_expression):
		"""
		convert the input string expression to tokens, and return this list
		Each token is either an integer operand or a character operator or bracket
		"""
		
		#for i in input_expression:
		#	if i in " ":
		#		self.l.append(i)
		#	
		#return self.l
		self.input_expression = input_expression
		self.input_expression = self.input_expression.replace(" ",'')
		self.tokens = []
		self.current_token = ""
    
		for char in self.input_expression:
			if char.isdigit():
				self.current_token += char
			elif char in ("+", "-", "*", "/", "(", ")", "{", "}"):
				if self.current_token != "":
					self.tokens.append(int(self.current_token))
					self.current_token = ""
				self.tokens.append(char)
		
		if self.current_token != "":
			self.tokens.append(int(self.current_token))
		return self.tokens
		
				
		pass		

	def check_brackets(self, list_tokens):
		"""
		check if brackets are valid, that is, all open brackets are closed by the same type 
		of brackets. Also () contain only () brackets.
		Return True if brackets are valid, False otherwise
		"""
		obj=Stack()
		for i in list_tokens:
			if i=="(" or i==")" or i=="{"or i=="}":
				obj.push(i)
		if(obj.__len__()%2!=0):
			return False
		r1=0
		c1=0
		a=0
		for i in range(obj.__len__()):
			s=obj.peek()
			obj.pop()
			if s=="{":
				c1+=1
				if(a!=0):
					return False
			elif s=="}":
				c1-=1
			elif s=="(":
				a+=1
				r1+=1
			else:
				r1-=1
				a=0	
			if(c1!=0 or r1!=0 or a!=0):
				return False
		return True


		pass

	def evaluate_list_tokens(self, list_tokens):
		"""
		Evaluate the expression passed as a list of tokens
		Return the final answer as a float, and "Error" in case of division by zero and other errors
		"""
		c=0
		for i in range(len(list_tokens)-1):
			if list_tokens[i] == "+" or list_tokens[i] == "-" or list_tokens[i] == "*" or list_tokens[i] == "/":
				if list_tokens[i+1] == "+" or list_tokens[i+1] == "-" or list_tokens[i+1] == "*" or list_tokens[i+1] == "/":
					return "Error"
				elif list_tokens[i+1] == ")" or list_tokens[i+1]=="}":
					return "Error"
		
		
		for i in list_tokens:
			if i not in ["+", "-", "*", "/", "(", ")", "{", "}","1","2","3","4","5","6","7","8","9","0"]:
				return "Error"
		for i in list_tokens:
			if i =="(" or  i ==")" or i=="{" or i=="}":
				c+=1
		if c==0:
			return super().evaluate_expression(list_tokens)
					
		

		
		operand=Stack()
		bracket=Stack()
		for i in list_tokens:
			if i in ")}":
				while (bracket.peek() not in "{("):
					result=0
					try:
						s=bracket.pop()
						if(s=="+"): result=float(operand.pop())+float(operand.pop())
						elif(s=="-"): result=float(operand.pop())-float(operand.pop())
						elif(s=="*"): result=float(operand.pop())*float(operand.pop())
						elif(s=="%"): result=float(operand.pop())%float(operand.pop())
					except ZeroDivisionError:
						return "Error"
					operand.push(result)
				if (bracket.peek() in "{("): bracket.pop()
			elif i.isnumeric():
				operand.push(i)
			elif i in "({"		:
				bracket.push(i)
			elif i in "+-*/":
				s="/*+-"
				if s.index(i)<s.index(bracket.peek()): bracket.push(i)
				else:
					result=0
					try:
						s=bracket.pop()
						if(s=="+"): result=float(operand.pop())+float(operand.pop())
						elif(s=="-"): result=float(operand.pop())-float(operand.pop())
						elif(s=="*"): result=float(operand.pop())*float(operand.pop())
						elif(s=="%"): result=float(operand.pop())%float(operand.pop())
					except ZeroDivisionError:
						return "Error"
					operand.push(result)
					bracket.push(i)
		return operand.peek()			


		pass

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.h[::-1]
		pass
