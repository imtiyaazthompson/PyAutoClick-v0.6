from pynput.mouse import Controller, Button

class Mouse():

	def __init__(self):
		self.mouse = Controller()
		self.x = self.mouse.position[0]
		self.y = self.mouse.position[1]
		self.pos = (self.x,self.y)


	def update(self):
		'''
			Update the mouses current position.
		'''
		self.x = self.mouse.position[0]
		self.y = self.mouse.position[1]
		self.pos = (self.x,self.y)

	def move_to(self,pos):
		'''
			Move the mouse to x2,y2
			Using  calculation to get the relative coords
			between (x1,y1) and (x2,y2).
		'''
		self.update()
		x1 = self.x
		y1 = self.y
		xr = pos[0] - x1
		yr = pos[1] - y1
		self.mouse.move(xr,yr)

	def left_single_click(self):
		'''
			Perform a single left click
			with the mouse.
		'''
		self.mouse.click(Button.left,1)

	def left_double_click(self):
		'''
			Perform a double click
			with the left mouse button.
		'''
		self.mouse.click(Button.left,2)

	def get_pos(self):
		'''
			Get the current position
			of the mouse.
		'''
		self.update()
		return self.pos