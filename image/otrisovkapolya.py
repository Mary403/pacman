import raylib
import pyray

from settings import Settings
from levels.levels import level1

def otr_pole(level=level1):
    x0 = Settings.WIDTH//2 - 5 * 32
    y0 = Settings.HEIGHT//2 - 5 * 32
    p = pyray.load_image('image/пустота.png')
    s1 = pyray.load_image('image/встена.png')
    s2 = pyray.load_image('image/лстена.png')
    s3 = pyray.load_image('image/пстена.png')
    s4 = pyray.load_image('image/нстена.png')
    ug1 = pyray.load_image('image/влугол.png')
    ug2 = pyray.load_image('image/впугол.png')
    ug3 = pyray.load_image('image/нлугол.png')
    ug4 = pyray.load_image('image/нпугол.png')

    pacman = pyray.load_image('image/пакман.png')

    p_texture = pyray.load_texture_from_image(p)
    s1_texture = pyray.load_texture_from_image(s1)
    s2_texture = pyray.load_texture_from_image(s2)
    s3_texture = pyray.load_texture_from_image(s3)
    s4_texture = pyray.load_texture_from_image(s4)
    ug1_texture = pyray.load_texture_from_image(ug1)
    ug2_texture = pyray.load_texture_from_image(ug2)
    ug3_texture = pyray.load_texture_from_image(ug3)
    ug4_texture = pyray.load_texture_from_image(ug4)
    pacman_texture = pyray.load_texture_from_image(pacman)

    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == "#":
                if j == 0:
                    if i == 0:
                        pyray.draw_texture(ug1_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)
                    elif i < len(level[i]) - 1:
                        pyray.draw_texture(s1_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)
                    else:
                        pyray.draw_texture(ug2_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)
                elif j < len(level) - 1:
                    if i == 0:
                        pyray.draw_texture(s3_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)
                    else:
                        pyray.draw_texture(s2_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)
                else:
                    if i == 0:
                        pyray.draw_texture(ug3_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)
                    elif i < len(level[i]) - 1:
                        pyray.draw_texture(s4_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)
                    else:
                        pyray.draw_texture(ug4_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)
            elif level[i][j] == " ":
                pyray.draw_texture(p_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)
            elif level[i][j] == "@":
                pyray.draw_texture(pacman_texture, x0 + i * 32, y0 + j * 32, pyray.WHITE)