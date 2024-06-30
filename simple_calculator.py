from stack import Stack

class SimpleCalculator:
	def __init__(self):
		"""
		Instantiate any data attributes
		"""
		self.history=[]
		self.s=""
		pass



	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		self.s="".join(input_expression.split())
		self.l=[i for i in self.s]
		
		self.x=0
		self.y=0
		c=0
		for i in self.l:
				if i not in "1234567890+-*/":
					self.history.append((input_expression,"Error"))
					return "Error"
				if i in "*-+/":
					c+=1
				if(c>1):
					self.history.append((input_expression,"Error"))
					return "Error"

		
		
		if self.l.count("+")==1:
			

			if(self.l.index("+")==0 or self.l.index("+")==len(self.l)-1):
				self.history.append((input_expression,"Error"))
				return "Error"
			
			for i in range(len(self.l)):
				if(i<self.l.index("+")):
					self.x=float(self.l[i])+self.x*10
				elif(i>self.s.index("+")):
					self.y=float(self.l[i])+self.y*10
				elif(self.l[i]!="+"):
					self.history.append((input_expression,"Error"))
					return "Error"	
			self.history.append((input_expression,float(self.x+self.y)))	
			return float(self.x+self.y)	

		elif self.l.count("-")==1:
			if(self.l.index("-")==0 or self.l.index("-")==len(self.l)-1):
				self.history.append((input_expression,"Error"))
				return "Error"
			
			for i in range(len(self.l)):
				if(i<self.l.index("-")):
					self.x=float(self.l[i])+self.x*10
				elif(i>self.s.index("-")):
					self.y=float(self.l[i])+self.y*10
				elif(self.l[i]!="-"):
					self.history.append((input_expression,"Error"))
					return "Error"
			self.history.append((input_expression,float(self.x-self.y)))	
			return float(self.x-self.y)	
		elif self.l.count("*")==1:
			if(self.l.index("*")==0 or self.l.index("*")==len(self.l)-1):
				self.history.append((input_expression,"Error"))
				return "Error"
			
			for i in range(len(self.l)):
				if(i<self.l.index("*")):
					self.x=float(self.l[i])+self.x*10
				elif(i>self.s.index("*")):
					self.y=float(self.l[i])+self.y*10
				elif(self.l[i]!="*"):
					self.history.append((input_expression,"Error"))
					return "Error"
			self.history.append((input_expression,float(self.x*self.y)))	
			return float(self.x*self.y)	
		elif self.l.count("/")==1:
			if(self.l.index("/")==0 or self.l.index("/")==len(self.l)-1):
				self.history.append((input_expression,"Error"))
				return "Error"
			
			for i in range(len(self.l)):
				if(i<self.l.index("/")):
					self.x=float(self.l[i])+self.x*10
				elif(i>self.s.index("/")):
					self.y=float(self.l[i])+self.y*10
				elif(self.l[i]!="/"):
					self.history.append((input_expression,"Error"))
					return "Error"
			if(self.y==0):
				self.history.append((input_expression,"Error"))
				return "Error"	
			self.history.append((input_expression,float(self.x/self.y)))	
			return float(self.x/self.y)	
		else:
			self.history.append((input_expression,"Error"))
			return "Error"
		
													
					
									



	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.history[::-1]
		pass
