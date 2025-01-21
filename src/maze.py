from cell import Cell
from math import floor
import time, random

class Maze():
	def __init__(
		self,
		x1,
		y1,
		num_rows,
		num_cols,
		cell_size_x,
		cell_size_y,
		seed=None,
		win=None,
	):
		self.x1 = x1
		self.y1 = y1
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.cell_size_x = cell_size_x
		self.cell_size_y = cell_size_y
		self.win = win
		random.seed(seed)
		self._create_cells()
	def _create_cells(self):
		self.cells = []
		for i in range(self.num_cols):
			col = []
			for j in range(self.num_rows):
				col.append(Cell(self.win))
			self.cells.append(col)
		for i in range(len(self.cells)):
			for j in range(len(self.cells[i])):
				self._draw_cell(i, j)
		self._break_entrance_and_exit()
		self._break_walls_r(0, 0)
		self._reset_cells_visited()
	def _draw_cell(self, i, j):
		cell = self.cells[i][j]
		x1 = self.x1+i*self.cell_size_x
		x2 = self.x1+(i+1)*self.cell_size_x
		y1 = self.y1+j*self.cell_size_y
		y2 = self.y1+(j+1)*self.cell_size_y
		print(f"drawing cell[{i}][{j}] at ({x1}, {y1}) ({x2}, {y2})")
		cell.draw(x1, x2, y1, y2)
		self._animate()
	def _animate(self):
		if (self.win):
			self.win.redraw()
			time.sleep(0.05)
	def _break_entrance_and_exit(self):
		entrance = self.cells[0][0]
		entrance.has_top_wall = False
		self._draw_cell(0, 0)
		exit = self.cells[self.num_cols-1][self.num_rows-1]
		exit.has_bottom_wall = False
		self._draw_cell(self.num_cols-1, self.num_rows-1)
	def _break_walls_r(self, i, j):
		self.cells[i][j].visited = True
		while True:
			not_visited = []
			for k in range(max(i-1, 0), min(i+2, self.num_cols)):
				for l in range(max(j-1, 0), min(j+2, self.num_rows)):
					if not self.cells[k][l].visited and (k == i or l == j):
						print(f"cell at ({k}, {l}) has not been visited")
						not_visited.append((k, l))
			if len(not_visited) == 0:
				print(f"no adjacent unvisited cells, returning")
				# time.sleep(5)
				return
			chosen = floor(random.random()*len(not_visited))
			# print(chosen)
			if chosen == len(not_visited):
				chosen = len(not_visited)-1
			new_i = not_visited[chosen][0]
			new_j = not_visited[chosen][1]
			
			if new_i > i:
				print(f"breaking right and left walls between ({i}, {j}) and ({new_i}, {new_j})")
				self.cells[i][j].has_right_wall = False
				self.cells[new_i][new_j].has_left_wall = False
			elif new_i < i:
				print(f"breaking left and right walls between ({i}, {j}) and ({new_i}, {new_j})")
				self.cells[i][j].has_left_wall = False
				self.cells[new_i][new_j].has_right_wall = False
			elif new_j > j:
				print(f"breaking bottom and top walls between ({i}, {j}) and ({new_i}, {new_j})")
				self.cells[i][j].has_bottom_wall = False
				self.cells[new_i][new_j].has_top_wall = False
			elif new_j < j:
				print(f"breaking top and bottom walls between ({i}, {j}) and ({new_i}, {new_j})")
				self.cells[i][j].has_top_wall = False
				self.cells[new_i][new_j].has_bottom_wall = False
			self._draw_cell(i, j)
			# time.sleep(5)
			self._break_walls_r(new_i, new_j)
		
	def _reset_cells_visited(self):
		for col in self.cells:
			for cell in col:
				cell.visited = False
	def _solve(self):
		self._solve_r(0, 0)
	def _solve_r(self, i, j):
		self._animate()
		self.cells[i][j].visited = True
		if i == self.num_cols-1 and j == self.num_rows-1:
			return True
		if i > 0 and not self.cells[i-1][j].visited and not self.cells[i][j].has_left_wall:
			self.cells[i][j].draw_move(self.cells[i-1][j])
			if self._solve_r(i-1, j):
				return True
			self.cells[i][j].draw_move(self.cells[i-1][j], True)
		if i < self.num_cols-1 and not self.cells[i+1][j].visited and not self.cells[i][j].has_right_wall:
			self.cells[i][j].draw_move(self.cells[i+1][j])
			if self._solve_r(i+1, j):
				return True
			self.cells[i][j].draw_move(self.cells[i+1][j], True)
		if j > 0 and not self.cells[i][j-1].visited and not self.cells[i][j].has_top_wall:
			self.cells[i][j].draw_move(self.cells[i][j-1])
			if self._solve_r(i, j-1):
				return True
			self.cells[i][j].draw_move(self.cells[i][j-1], True)
		if j < self.num_rows-1 and not self.cells[i][j+1].visited and not self.cells[i][j].has_bottom_wall:
			self.cells[i][j].draw_move(self.cells[i][j+1])
			if self._solve_r(i, j+1):
				return True
			self.cells[i][j].draw_move(self.cells[i][j+1], True)
		return False
		
