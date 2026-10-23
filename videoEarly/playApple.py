from time import sleep
import sys

CLEAR_SCREEN = "\033[2J"
CURSOR_TOP_LEFT = "\033[H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

sys.stdout.write(HIDE_CURSOR)
sys.stdout.write(CLEAR_SCREEN)
sys.stdout.flush()

out = []

with open("bad_apple.txt", "r") as file:
	for line in file:
		out.append(line)

try:
	for a in out:
		if a == ";\n":
			sys.stdout.flush()
			sleep(0.03244444)
			sys.stdout.write(CLEAR_SCREEN)
			sys.stdout.write(CURSOR_TOP_LEFT)
			sys.stdout.flush()
		else:
			sys.stdout.write("		     ")
			sys.stdout.write(a)

finally:
	sys.stdout.write(SHOW_CURSOR)
	sys.stdout.flush()
