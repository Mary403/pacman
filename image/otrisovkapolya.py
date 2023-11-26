import raylib
import pyray

from settings import Settings
from objects.levels import level1


def otr_pole(level=level1):
    x0 = Settings.WIDTH//2 - 4 * 52
    y0 = Settings.HEIGHT//2 - 4 * 48
    p = pyray.load_image('image/pustota.png')
    s = pyray.load_image('image/stena.png')
    s2 = pyray.load_image('image/stena_vniz.png')
    ug1 = pyray.load_image('image/ugol1.png')
    ug2 = pyray.load_image('image/ugol2.png')
    ug3 = pyray.load_image('image/ugol3.png')
    ug4 = pyray.load_image('image/ugol4.png')

    p_texture = pyray.load_texture_from_image(p)
    s_texture = pyray.load_texture_from_image(s)
    s2_texture = pyray.load_texture_from_image(s2)
    ug1_texture = pyray.load_texture_from_image(ug1)
    ug2_texture = pyray.load_texture_from_image(ug2)
    ug3_texture = pyray.load_texture_from_image(ug3)
    ug4_texture = pyray.load_texture_from_image(ug4)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == "|":
                pyray.draw_texture(s_texture, x0 + i * 52, y0 + j * 48, pyray.WHITE)
            elif level[i][j] == "-":
                pyray.draw_texture(s2_texture, x0 + i * 52, y0 + j * 48, pyray.WHITE)
            elif level[i][j] == "1":
                pyray.draw_texture(ug1_texture, x0 + i * 52, y0 + j * 48, pyray.WHITE)
            elif level[i][j] == "2":
                pyray.draw_texture(ug3_texture, x0 + i * 52, y0 + j * 48, pyray.WHITE)
            elif level[i][j] == "3":
                pyray.draw_texture(ug2_texture, x0 + i * 52, y0 + j * 48, pyray.WHITE)
            elif level[i][j] == "4":
                pyray.draw_texture(ug4_texture, x0 + i * 52, y0 + j * 48, pyray.WHITE)