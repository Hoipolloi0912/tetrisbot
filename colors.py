class Colors:
    gray = (26,31,40)
    green = (83,218,63)
    red = (234,20,28)
    orange = (255,145,12)
    yellow = (254,251,52)
    purple = (221,10,178)
    cyan = (1,237,250)
    blue = (0,119,211)
    white = (255,255,255)

    @classmethod
    def get_colors(cls):
        return [cls.gray,cls.green,cls.red,cls.orange,
                cls.yellow,cls.purple,cls.cyan,cls.blue,cls.white]