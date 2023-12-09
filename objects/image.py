import pyray

from objects.base import BaseObject


class Image(BaseObject):
    def __init__(self, path: str, rect: pyray.Rectangle):
        super().__init__(rect.x, rect.y)
        self.width = rect.width
        self.height = rect.height
        pic = pyray.load_image(path)
        self.texture = pyray.load_texture_from_image(pic)
        pyray.unload_image(pic)
        self.rotation = 0

    def draw(self):
        source = pyray.Rectangle(0, 0, self.texture.width, self.texture.height)
        dest = pyray.Rectangle(self.x, self.y, self.width, self.height)
        origin = pyray.Vector2(self.width // 2, self.height // 2)
        pyray.draw_texture_pro(self.texture, source, dest, origin, self.rotation, pyray.Color(*[255] * 4))

    def set_picture(self, path):
        pic = pyray.load_image(path)
        self.texture = pyray.load_texture_from_image(pic)
        pyray.unload_image(pic)

    def set_rotation(self, rot):
        self.rotation = rot
