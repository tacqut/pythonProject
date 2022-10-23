class Point:
    color1 = 'red'
    circle = 2

    @classmethod
    def validate(cls, arg):
        return cls.color1 == arg

    def __new__(cls, *args, **kwargs):
        print("Вызов new для: " + str(cls))
        return super().__new__(cls)

    def __init__(self, a, b, cl):
        self.x = self.y = 0
        self.color = "red"
        if not self.validate(cl):
            self.x = a
            self.y = b
            self.color = cl

    def __del__(self):
        print("Удаление экземпляра: " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        print(self.x, self.y)
