from vanilla_api.sprites.button import Button


class VanillaSprite(Button):
    def __init__(self, pos):
        super().__init__(pos,
                         (600, 600),
                         "assets/icon.png",
                         "assets/icon1.png",
                         "assets/icon2.png",
                         lambda: print("Hello Button"))
