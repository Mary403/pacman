from scenes.base import BaseScene
from settings import Settings

from game_objects.pole import LogicPole
from game_objects.field import FieldDrawer
from game_objects.seeds import *

from objects.figure import *
from objects.text import Text
from objects.button_menu import ButtonMenu
from objects.button_pause import ButtonPause
from game_objects.counter import Counter


class GameScene(BaseScene):  # Сцена 2
    def __init__(self):
        self.pole = LogicPole()
        self.pac_logic = self.pole.pacman
        self.pac_image = self.pole.pacman.image_pacman
        self.ghost_image = self.pole.ghost.image_ghost
        self.button_menu = ButtonMenu()
        self.button_pause = ButtonPause()

        self.rec = Rect((Settings.WIDTH - 17 * 30) // 2, (Settings.HEIGHT - 21 * 30) // 2,
                        Settings.WIDTH - (Settings.WIDTH - 17 * 30), Settings.HEIGHT - (Settings.HEIGHT - 21 * 30),
                        colors.BLUE, True)

        self.field_drawer = FieldDrawer(self.pole.data)
        self.seeds = SeedsLogic()

        self.gameover_text = Text(Settings.WIDTH // 2 - 230, Settings.HEIGHT // 2 - 50, "EASY WIN!", 100,
                                  (10, 200, 50, 255))
        self.rec_gameover = Rect((Settings.WIDTH - 17 * 30) // 2, (Settings.HEIGHT - 21 * 30) // 2,
                                 Settings.WIDTH - (Settings.WIDTH - 17 * 30),
                                 Settings.HEIGHT - (Settings.HEIGHT - 21 * 30),
                                 (0, 0, 0, 160), False)

        self.counter = Counter(300, 30)

        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.pole)
        self.objects.append(self.button_menu)
        self.objects.append(self.button_pause)
        self.objects.append(self.field_drawer)
        self.objects.append(self.pac_image)
        self.objects.append(self.seeds)
        self.objects.append(self.counter)
        self.objects.append(self.ghost_image)

    def newgame(self):
        self.pole.newgame()
        self.pac_image.newgame()
        self.pac_logic.newgame()
        self.counter.newgame()
        self.seeds.newgame()

        if self.rec_gameover in self.objects:
            self.objects.remove(self.rec_gameover)
        if self.gameover_text in self.objects:
            self.objects.remove(self.gameover_text)
        Settings.is_gameover = False

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ZERO):
            Settings.set_scene(0)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            Settings.set_scene(1)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_THREE):
            Settings.set_scene(3)

        if Settings.newgame:
            Settings.newgame = False
            self.newgame()

        for i in range(len(self.seeds.seeds)):
            c1 = self.seeds.seeds[i].get_center()
            c2 = self.pac_image.get_center()
            r1 = self.seeds.seeds[i].get_radius()
            r2 = self.pac_image.get_radius()

            if pyray.check_collision_circles(c1, r1, c2, r2):
                self.seeds.seeds[i].eaten(self.counter)
                self.seeds.seeds.remove(self.seeds.seeds[i])
                break
        if len(self.seeds.seeds) <= 0:
            if not Settings.is_gameover:
                print(len(self.seeds.seeds))
                self.gameover()

        # TODO: Событие коллизии с призраком


    def gameover(self):
        self.objects.append(self.rec_gameover)
        self.objects.append(self.gameover_text)
        Settings.is_gameover = True
