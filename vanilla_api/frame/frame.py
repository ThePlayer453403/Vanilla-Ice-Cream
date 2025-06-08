import sys
import json
import pygame
from pygame.locals import *
from vanilla_api.emoji import emoji


class VanillaIceCream:
    def __init__(self):
        # 初始化pygame
        if not pygame.get_init():
            pygame.init()
            # 打印没什么卵用的日志（*＾3＾）/～☆
            print("Hello from Vanilla Ice Cream. https://github.com/ThePlayerZhang/Vanilla-Ice-Cream " + emoji.qwq())

        # 导入设置文件
        # 设置文件解析
        #     "title":      窗口的标题
        #     "icon":       窗口的图标, 填写路径
        #     "size":       窗口分辨率, 填写列表
        #     "background": 背景, 填写列表, 第一个元素填写类型("color"或"texture"), 第二个元素填写颜色列表(color)或图片路径(texture)
        #     "flags":      窗口的属性
        #             fullscreen 创建全屏显示
        #             doublebuf 仅适用于 OPENGL
        #             opengl 创建 OpenGL 可渲染的显示器
        #             resizeable 显示窗口应为 sizeable
        #             oframe 显示窗口将没有边框或控件
        #             scaled 分辨率取决于桌面大小和缩放图形
        #             shown 窗口以可见模式打开（默认）
        #             hidden 窗口以隐藏模式打开
        with open("./vanilla_config/frame.json", "r", encoding="utf-8") as config:
            self.config = json.load(config)
        self.display = pygame.display.set_mode(self.config["size"], eval("|".join(self.config["flags"]).upper() or "0"))
        pygame.display.set_caption(self.config["title"])
        pygame.display.set_icon(pygame.image.load(self.config["icon"]))

        self.update = pygame.display.update

        self.sprites = []
        self.level = {}

    def load_level(self, name):
        with open("assets/data/levels/"+name+".json", "r", encoding="utf-8") as level:
            self.level = json.load(level)
        for sprite in self.level["objects"]:
            obj = __import__("assets.data.sprites."+sprite["id"], fromlist=["VanillaSprite"])
            self.sprites.append(obj.VanillaSprite(*sprite["data"]))

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_background()

            mouse = [pygame.mouse.get_pos(), pygame.mouse.get_pressed()]
            for sprite in self.sprites:
                sprite.tick(mouse=mouse)
                sprite.render(self.display)

            self.tick()
            self.update()

    def tick(self):
        pass

    def resize(self, x, y):
        self.display = pygame.display.set_mode((x, y))
        return self

    def set_flags(self, flags):
        self.display = pygame.display.set_mode(flags=flags)
        return self

    def draw_background(self):
        if self.config["background"][0] == "color":
            self.display.fill(self.config["background"][1])
