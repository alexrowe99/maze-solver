from window import Window
from maze import Maze
import time


def main():
	w = Window(1000, 1000)
	m = Maze(100, 100, 9, 9, 100, 100, time.time(), w)
	m._solve()
	w.wait_for_close()

if __name__ == "__main__":
	main()
