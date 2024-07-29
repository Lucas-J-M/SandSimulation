import pygame as py
class sandgame:
    def __init__(self: int, grid_size: int, window_width: int, window_height: int, surface, grid_color) -> None:
        for x in range(0, window_width, grid_size):
            for y in range(0, window_height, grid_size):
                gridblock = py.Rect(x, y, grid_size, grid_size)
                py.draw.rect(surface, grid_color, gridblock, 1)
        self.grid_size = grid_size
        self.window_height = window_height
        self.window_width = window_width
        self.grid_color = grid_color
        self.surface = surface
    def createsand(self, mouse_position: tuple):
        posx, posy = (((mouse_position[0] // self.grid_size) * self.grid_size), ((mouse_position[1] // self.grid_size) * self.grid_size))

        sandblock = py.Rect(posx, posy, self.grid_size, self.grid_size)
        py.draw.rect(self.surface, self.grid_color, sandblock)
    def updatesandposition(self, new_pos: tuple):
        sandblock = py.Rect(new_pos[0], new_pos[1], self.grid_size, self.grid_size)
        py.draw.rect(self.surface, self.grid_color, sandblock)
        coverblock = py.Rect(new_pos[0], new_pos[1] - self.grid_size, self.grid_size, self.grid_size)
        py.draw.rect(self.surface, py.Color(0,0,0), coverblock)
