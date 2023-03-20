from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 1
        self.fly_time = 0
        super().__init__(images, self.type)

        self.rect.y = 215

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
        self.fly_time +=1
        if self.fly_time >= 10:
            self.type = 0
            if self.fly_time >= 20:
                self.type = 1
                self.fly_time = 0




