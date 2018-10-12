from Record import Record
import time

class ClickAutomator():

	def __init__(self,record=Record(),delay_btw_caps=0,delay_btw_reps=0,repeats=1):
		self.record = record
		self.delay_btw_caps = delay_btw_caps
		self.delay_btw_reps = delay_btw_reps
		self.repeats = repeats


	def automate(self):
		'''
			Start the automation process
		'''
		x = 0
		y = 0
		while True:
			x = self.main_menu()
			if x == 4:
				break
			else:
				y = self.sub_menu(x)

		self.record.record()
		points = self.record.records
		print(points)

		reps = 0
		while reps != self.repeats:
			for point in points:
				self.record.mouse.move_to(point)
				self.record.mouse.left_single_click()
				time.sleep(self.delay_btw_caps)
			reps += 1

	def main_menu(self):
		'''
			Main menu for the program
		'''
		print('PyClickAuto v0.6\nby Imtiyaaz Thompson\n')
		print('[1] Set time delay (seconds) between each click')
		print('[2] Set time delay (seconds) between each repetition')
		print('[3] Set the number of repetitions')
		print('[4] Start PyClickAuto')
		print('[5] Reset all values to default')
		choice = 0
		while True:
			try:
				choice = int(input('>>'))
			except:
				continue
			else:
				break
		
		return choice

	def sub_menu(self,c):
		'''
			Sub menu
		'''
		if c == 1:
			print('Set delay between each click.')
			while True:
				try:
					self.delay_btw_caps = float(input('>>'))
				except:
					continue
				else:
					break
		elif c == 2:
			print('Set delay between each repetition.')
			while True:
				try:
					self.delay_btw_reps = float(input('>>'))
				except:
					continue
				else:
					break
		elif c == 3:
			print('Set the number of repetitions.')
			while True:
				try:
					self.repeats = int(input('>>'))
				except:
					continue
				else:
					break
		elif c == 5:
			print('All values set to default.')
			self.delay_btw_caps = 0
			self.delay_btw_reps = 0
			self.repeats = 1

if __name__ == '__main__':
	ca = ClickAutomator()
	ca.automate()