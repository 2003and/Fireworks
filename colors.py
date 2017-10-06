class Colors:
    def __init__(self):
        self.white = [255, 255, 255]
        self.black = [0, 0, 0]
        self.gray = [150, 150, 150]
        self.dark_gray = [100, 100, 100]
        self.very_dark_gray = [50, 50, 50]

        self.pink = [255, 200, 200]
        self.red = [255, 0, 0]
        self.dark_red = [200, 0, 0]
        self.purple = [200, 0, 200]

        self.blue = [0, 0, 255]
        self.light_blue = [70, 70, 255]
        self.very_light_blue = [140, 140, 255]
        self.dark_blue = [0, 0, 200]

        self.brown = [153, 76, 0]
        self.light_brown = [203, 126, 0]
        self.yellow = [255, 255, 0]
        self.a_bit_darker_yellow = [230, 230, 0]
        self.orange = [255, 175, 0]

        self.green = [0, 255, 0]
        self.light_green = [100, 255, 100]
        self.lime = [175, 255, 0]
        self.dark_green = [0, 200, 0]

        self.magenta = [255, 0, 200]

        self.custom = []

    def new_color(self, r, g, b):
        self.custom.append([r, g, b])

    def delete_color(self, which):
        self.custom.pop(which)
