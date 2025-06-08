from vanilla_api.frame import frame


class VanillaIceCream(frame.VanillaIceCream):
    def __init__(self):
        super().__init__()
        self.load_level("menu")
        self.mainloop()

    def tick(self):
        pass


if __name__ == "__main__":
    VanillaIceCream()
