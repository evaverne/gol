from graphics import *

def main():
	win = GraphWin("Game of Life", 500, 500)

	#grid = [ [-1]*10  for n in range(10)]
	
	#for one in grid:
	rect = Rectangle (Point(0,0), Point (20,20))
	rect.setOutline('black')
	rect.draw(win)

	 


	win.getMouse()
	win.close()

main()