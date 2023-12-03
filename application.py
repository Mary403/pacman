import pyray

from scenes.menu import MenuScene
from scenes.pause import PauseScene
from settings import Settings


class Application:
    def __init__(self):
        pyray.init_window(Settings.WIDTH, Settings.HEIGHT, "Pacman")
        pyray.set_target_fps(Settings.FPS)
        self.game_over = False
        self.scenes = [
            MenuScene(),
            PauseScene(),
        ]

    def scene_activate(self):
        Settings.scene_changed = False
        self.scenes[Settings.scene_index].activate()

    def scene_event(self):
        self.scenes[Settings.scene_index].process_event()
        if pyray.window_should_close() or pyray.is_key_pressed(pyray.KeyboardKey.KEY_ESCAPE):
            self.game_over = True

    def scene_logic(self):
        self.scenes[Settings.scene_index].process_logic()

    def scene_draw(self):
        pyray.begin_drawing()
        pyray.clear_background(Settings.BACKGROUND_COLOR)
        self.scenes[Settings.scene_index].process_draw()
        pyray.end_drawing()

    def process_frame(self):
        if Settings.scene_changed:
            self.scene_activate()
        self.scene_event()
        self.scene_logic()
        self.scene_draw()

    def run(self):
        while not self.game_over:
            self.process_frame()
        pyray.close_window()
