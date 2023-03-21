import random
import pygame

from dino_runner.components.obstacles.cactus import Small_Cactus
from dino_runner.components.obstacles.cactus import Large_Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.obstacle_type = random.randint(0, 2)
        if len(self.obstacles) == 0 and self.obstacle_type == 0:
            self.obstacles.append(Small_Cactus(SMALL_CACTUS))
        if len(self.obstacles) == 0 and self.obstacle_type == 1:
            self.obstacles.append(Large_Cactus(LARGE_CACTUS))
        if len(self.obstacles) == 0 and self.obstacle_type == 2:
            self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count+=1
                break                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles.clear()
