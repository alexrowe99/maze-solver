from point import Point
from line import Line
from constants import MAZE_COLOUR

class Cell():
	def __init__(
		self,
		_x1,
		_x2,
		_y1,
		_y2,
		_win,
		has_left_wall=True,
		has_right_wall=True,
		has_top_wall=True,
		has_bottom_wall=True,
	):
		self.has_left_wall = has_left_wall
		self.has_right_wall = has_right_wall
		self.has_top_wall = has_top_wall
		self.has_bottom_wall = has_bottom_wall
		self._x1 = _x1
		self._x2 = _x2
		self._y1 = _y1
		self._y2 = _y2
		self._win = _win
	def draw(self):
		if self.has_bottom_wall:
			bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
			self._win.draw_line(bottom_wall, MAZE_COLOUR)
		if self.has_left_wall:
			left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
			self._win.draw_line(left_wall, MAZE_COLOUR)
		if self.has_right_wall:
			right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
			self._win.draw_line(right_wall, MAZE_COLOUR)
		if self.has_top_wall:
			top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
			self._win.draw_line(top_wall, MAZE_COLOUR)