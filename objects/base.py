class BaseObject:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def activate(self):
        """
        Метод инициализирующий проект
        """
        pass

    def event(self):
        """
        Метод для обработки событий объекта.
        """
        pass

    def logic(self):
        """
        Метод для обработки логики объекта.
        """
        pass

    def draw(self):
        """
        Метод для отрисовки объекта.
        """
        pass
