from Mouse import Mouse
from pynput import keyboard


class Record():

	def __init__(self,mouse=Mouse(),rec_k='c',quit_k='q'):
		self.mouse = mouse
		self.rec_k = rec_k
		self.quit_k = quit_k
		self.records = []

	def get_keycode(self,key):
		'''
			Gets the key code for the 
			corresponding character.
		'''
		return keyboard.KeyCode.from_char(key)

	def on_press(self,key):
		'''
			Actions performed on the press of the 
			record key - key.
		'''
		if key == self.get_keycode(self.rec_k):
			pass

	def on_release(self,key):
		'''
			Actions performed on the release of the 
			record key key
		'''
		if key == self.get_keycode(self.rec_k):
			print('Point recorded.')
			self.records.append(self.mouse.get_pos())
		elif key == self.get_keycode(self.quit_k):
			return False

	def record(self):
		'''
			Start the mouse position record process.
		'''
		print('Recording process started\npress:' + self.rec_k + ' to record a position' )
		print('press:' + self.quit_k + ' to stop recording' )

		with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener: listener.join()