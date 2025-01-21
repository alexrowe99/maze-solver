from point import Point
from line import Line
from constants import MAZE_COLOUR, LINE_COLOUR, UNDO_COLOUR

class Cell():
	def __init__(
		self,
		_win=None,
		has_left_wall=True,
		has_right_wall=True,
		has_top_wall=True,
		has_bottom_wall=True,
	):
		self.has_left_wall = has_left_wall
		self.has_right_wall = has_right_wall
		self.has_top_wall = has_top_wall
		self.has_bottom_wall = has_bottom_wall
		self._win = _win
		self.visited = False
	def draw(self, _x1, _x2, _y1, _y2):
		self._x1 = _x1
		self._x2 = _x2
		self._y1 = _y1
		self._y2 = _y2
		bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
		left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
		right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
		top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
		if (self._win):
			if self.has_bottom_wall:
				self._win.draw_line(bottom_wall, MAZE_COLOUR)
			else:
				self._win.draw_line(bottom_wall, self._win.root["bg"])
			if self.has_left_wall:
				self._win.draw_line(left_wall, MAZE_COLOUR)
			else:
				self._win.draw_line(left_wall, self._win.root["bg"])
			if self.has_right_wall:
				self._win.draw_line(right_wall, MAZE_COLOUR)
			else:
				self._win.draw_line(right_wall, self._win.root["bg"])
			if self.has_top_wall:
				self._win.draw_line(top_wall, MAZE_COLOUR)
			else:
				self._win.draw_line(top_wall, self._win.root["bg"])
	def draw_move(self, to_cell, undo=False):
		line = Line(Point(self._x1+((self._x2-self._x1)/2), self._y1+((self._y2-self._y1)/2)), Point(to_cell._x1+((to_cell._x2-to_cell._x1)/2), to_cell._y1+((to_cell._y2-to_cell._y1)/2)))
		if (undo):
			self._win.draw_line(line, UNDO_COLOUR)
		else:
			self._win.draw_line(line, LINE_COLOUR)