import raylib


class BaseScene:
    def __init__(self):
        self.objects = []
        self.set_up_objects()

    def set_up_objects(self):
        pass

    def activate(self):
        for item in self.objects:
            item.activate()
        self.additional_activate()

    def additional_activate(self):
        pass

    def process_event(self):
        for item in self.objects:
            item.event()
        self.additional_process_event()

    def additional_process_event(self):
        pass

    def process_logic(self):
        for item in self.objects:
            item.logic()
        self.process_additional_logic()

    def process_additional_logic(self):
        pass

    def process_draw(self):
        for item in self.objects:
            item.draw()
        self.process_additional_draw()

    def process_additional_draw(self):
        pass
