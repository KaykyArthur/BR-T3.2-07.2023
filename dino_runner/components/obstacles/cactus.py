import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Small_Cactus(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,2)
        super().__init__(images, self.type)

        self.rect.y = 325

class Large_Cactus(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,2)
        super().__init__(images, self.type)

        self.rect.y = 300

