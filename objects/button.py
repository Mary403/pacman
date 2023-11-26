import pyray
from pyautogui import Point
from raylib import colors
from figure import Rect
import pyautogui

"""
Класс кнопки
"""

class Button(Rect):
    def __init__(self, x, y, width, height, color=None, outline=False):
        super().__init__(x, y, width, height, color, outline)

    def set_size(self, w, h):
        self.__width = w
        self.__height = h

    def draw(self):
        draw_func = pyray.draw_rectangle if not self.__outline else pyray.draw_rectangle_lines
        draw_func(self.x, self.y, self.__width, self.__height, self.__color)

    def event(self):
        if self.is_click():
            self.click()
        pass

    def is_click(self):  # проверка нажата ли кнопка
        point: Point = pyautogui.position()
        rec = (self.x, self.y, self.__width, self.__height)
        if pyray.check_collision_point_rec(point, rec):
            if pyray.is_key_down(pyray.is_mouse_button_down(1)):
                return True
            return False
        return False


    def click(self): #  событие клика
        pass


