from vanilla_api.frame import frame
from vanilla_api.sprites import button


class VanillaIceCream(frame.VanillaIceCream):
    def __init__(self):
        super().__init__()
        self.load_level("menu")
        self.mainloop()

    def tick(self):
        pass


if __name__ == "__main__":
    VanillaIceCream()
