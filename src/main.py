from window import Window
from line import Line
from point import Point

def main():
	w = Window(800, 600)
	w.draw_line(Line(Point(0,0), Point(400,300)), "red")
	w.wait_for_close()

if __name__ == "__main__":
	main()
