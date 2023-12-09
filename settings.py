from raylib import colors


class Settings:
    WIDTH = 1000
    HEIGHT = 800
    FPS = 60
    BACKGROUND_COLOR = colors.BLACK
    scene_changed = True
    scene_index = 1

    @staticmethod
    def set_scene(index):
        Settings.scene_changed = True
        Settings.scene_index = index

    @staticmethod
    def set_game_scene():
        Settings.set_scene(1)
