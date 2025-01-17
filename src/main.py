from window import Window
from cell import Cell


def main():
	w = Window(1500, 1500)
	walls = [
		[False, False, False, False],
		[True, False, False, False],
		[False, True, False, False],
		[False, False, True, False],

		[False, False, False, True],
		[True, True, False, False],
		[True, False, True, False],
		[True, False, False, True],

		[False, True, True, False],
		[False, True, False, True],
		[False, False, True, True],
		[True, True, True, False],

		[True, True, False, True],
		[True, False, True, True],
		[False, True, True, True],
		[True, True, True, True]
	]
	for i in range(0, 4):
		for j in range(0, 4):
			Cell((j+1)*100, (i+1)*100, (j+2)*100, (i+2)*100, w, walls[i][0], walls[i][1], walls[i][2], walls[i][3]).draw()

	w.wait_for_close()

if __name__ == "__main__":
	main()
