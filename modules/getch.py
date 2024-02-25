class _Getch:
	"""
	Gets a single character from standard input. Does not echo to the screen.
	Unlike raw_input(), does not require the enter key to be pressed in order
	to work.
	
	Usage:
	getch.getch() Waits for user input of a single character, and returns the
	character the user entered (which can then be stored in a variable name)
	"""
	def __init__(self):
		self.impl = _GetchUnix()
	def __call__(self): return self.impl()

class _GetchUnix:
	def __init__(self):
		import tty, sys

	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

getch = _Getch()
