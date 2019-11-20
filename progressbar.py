import sys
# Create a progress Bar like this:
# [■■■■■■■■■■          ] 50%
# Initialize new bar object with a max "done" value
# Update with progress to max
# No error checking for things like over 100% conditions, might add later
class Bar():
	def __init__(self,max):
		#Max value to finish progress bar
		self.max = max
		#Old and new values are tracker values
		self.old = 0
		#Default width for the bar
		self.width = 50
		#Default value is 0
		self.count = 0

	def update(self,new):
		#new percent
		n = round(float(new) / float(self.max) * 100)
		#old percent
		o = round(float(self.old) / float(self.max) * 100)
		#count of the number of tickers, normalized to width of the bar
		count = int(round((n - o)/(100 / self.width)))
		#m = number of spaces after the blocks before brackets
		m = self.width - count
		#calculate the percent complete
		p = int(round(100*(float(new)) / float(self.max)))
		#chr(9632) is the unicode decimal code for Black Square
		sys.stdout.write("\r[{0}{1}] {2}%".format(chr(9632)*count," "*m,p))

