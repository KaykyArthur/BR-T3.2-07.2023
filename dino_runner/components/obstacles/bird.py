import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images, bird_position):
        self.type = 1
        self.fly_time = 0
        super().__init__(images, self.type)

        self.touched_ground = False
        self.moving = random.randint(1,2) % 2 == 0 and True or False

        self.rect.y = bird_position

    def update(self,game_speed, obstacles):
        if self.moving:
            if not self.touched_ground:
                self.rect.y +=10
                if self.rect.y > 350:
                    self.touched_ground = True
            else:
                self.rect.y -=10
                if self.rect.y < 200:
                    self.touched_ground = False

        super().update(game_speed, obstacles)

    def draw(self, screen):
        self.fly_time +=1
        if self.fly_time >= 10:
            self.type = 0
            if self.fly_time >= 20:
                self.type = 1
                self.fly_time = 0
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))




